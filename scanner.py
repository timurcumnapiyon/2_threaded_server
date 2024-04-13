import socket
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

N = 2**16 - 1

for port in range(1,100):
    sock = socket.socket()
def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        print(port)
        sock.connect(('127.0.0.1', port))
        print("Порт", i, "открыт")
    except:
        continue
        result = sock.connect_ex((host, port))
        if result == 0:
            return port
        else:
            return None
    except Exception as e:
        return None
    finally:
        sock.close()

        sock.close()
        
def scan_ports(host):
    open_ports = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []
        for port in range(1, 100):
            futures.append(executor.submit(scan_port, host, port))
        for future in tqdm(futures, total=len(futures), desc="Scanning"):
            result = future.result()
            if result:
                open_ports.append(result)
    return open_ports

if __name__ == "__main__":
    host = input("Enter the host/IP address to scan: ")
    open_ports = scan_ports(host)
    print("Open ports:", open_ports)

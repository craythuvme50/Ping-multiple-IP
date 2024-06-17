#!/usr/bin/python3

from pythonping import ping
from datetime import datetime

file = 'ip_list.txt'

def read_ip(file):
  with open (file, 'r') as ip_list:
    return [line.strip() for line in ip_list]

ip_address = read_ip(file)

current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"ping_results_{current_datetime}.txt"

with open(output_file, 'w+') as f:
    for ip in ip_address:
        ping_result = ping(ip, count=2, timeout=0.5)
        f.write(str(ping_result) + "\n")
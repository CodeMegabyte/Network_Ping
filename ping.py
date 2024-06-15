import os
ip1 = input("Enter first IP: ")
ip2 = input("Enter Second IP: ")
ip_list = [ip1, ip2, "127.0.0.1"]
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"UP {ip} Ping Successful")
    else:
        print(f"DOWN {ip} Ping Unsuccessful")
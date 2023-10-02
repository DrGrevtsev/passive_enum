#Welcome to passive enum, that is going to help you with your reconn.

import os
import whois
import socket

def domain():
    hostname = input("choose a domain name or ip you want to work on: ")
    return hostname

def domain_check(hostname):
    ping_rec = os.system('ping -c 1 ' + hostname)
    for ping in str(ping_rec):
        if ping == 0:
            print(f'{hostname} is up!')
            break
        else:   
            print(f'{hostname} is down!')
            break
        
def who_is_domain(hostname):
        host_info = whois.whois(hostname)
        print(host_info)   
        return host_info

def who_is_dns(hostname):
    while True:
        if socket.gethostbyaddr(hostname):
            print(socket.gethostbyaddr(hostname))
            break
        elif socket.gethostbyname(hostname):
            print(socket.gethostbyname(hostname)) 
            break   
            
def get_info(hostname):
    work_status = domain_check(hostname)
    print("The Following Domain Record:\n")
    who_is_domain(hostname)
    print("The Following DNS Record:\n")
    who_is_dns(hostname)
    
def brute_force(host_info):
    for dns in host_info:
        dns_check = who_is_domain(dns)
        if "NetRange" in dns_check:
            print(dns_check["NetRange"])
        
              
def main():
    try:
        hostname = domain()
        host_info = who_is_domain(hostname)
        get_info(hostname)
        brute_force(host_info)
    except KeyboardInterrupt:
        print("see you..")
main() 
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

vlanStart = 1000
vlanStop = 1025
host="203.209.48.2"

L2 = Ether(src="",dst="")
L3 = IP(dst=host)

for i in range(vlanStart,vlanStop):
    vid="VLAN ID:" + str(i)
    sendp(L2/Dot1Q(vlan=i)/L3/ICMP()/vid)
print("Complete!!")
#! /usr/bin/env python3

import psutil
import socket

def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    print("DEBUG: Hostname: {} Usage: {}".format(socket.gethostname(),usage))
    return usage < percent

if not check_cpu_usage(50):
    print("ERROR! CPU is overloaded")
else:
    print("Everything is OK!")



#
# jnap-demo.py - demonstrate methods in the jnap library
# by Jake Kara
# February 2018
# jake@jakekara.com
#

from jnap.router import Linksys 
from time import sleep
import json
import sys
import getpass
 
addr = sys.argv[1]
router = Linksys(addr)

pw = getpass.getpass("Enter admin password for '"+str(addr)+"': ")
router.password(pw)
print (json.dumps(router.check_password(pw).json(), indent=2))

# Checking whether router has default password
print (json.dumps(router.has_default_password().json(), indent=2))

# Listing all users
print (json.dumps(router.get_users().json(), indent=2))

# Getting a bunch of device info
print (json.dumps(router.get_device_info().json(), indent=2))

# Testing out the ping functionality
print (json.dumps(router.stop_ping().json(), indent=2))
print (json.dumps(router.start_ping(host="192.168.1.197",count=10).json(), indent=2))

# Check every 2 seconds to see if ping is done. TIMEOUT after 1 minute
TIMEOUT=60
SLEEPFOR=2

while TIMEOUT > 0:
    status = router.get_ping_status().json()["output"]["isRunning"]
    if status != True: break
    else:
        print ("Still pinging: " + str(status))
    TIMEOUT -= SLEEPFOR
    sleep(SLEEPFOR)

print (json.dumps(router.get_ping_status().json(), indent=2))
print (json.dumps(router.stop_ping().json(), indent=2))

# Test out the traceroute functionality from the router to google.com
print (json.dumps(router.stop_traceroute().json(), indent=2))
print (json.dumps(router.start_traceroute("google.com").json(), indent=2))

# Reset the clock
TIMEOUT = 60
while TIMEOUT > 0:
    status = router.get_traceroute_status().json()["output"]["isRunning"]
    if status != True: break
    else:
        print ("Still tracing: " + str(status))
    TIMEOUT -= SLEEPFOR
    sleep(SLEEPFOR)

print (json.dumps(router.stop_traceroute().json(), indent=2))
print (json.dumps(router.get_traceroute_status().json(), indent=2))




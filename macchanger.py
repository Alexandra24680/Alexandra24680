#!/usr/bin/env python

import subprocess
import optparse
import re
import pyfiglet

def get_arguements():

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", help="Interface to change the MAC Address", dest="interface")
    parser.add_option("-m", "--mac", help="New MAC Address to be set", dest="new_mac")
    (options, arguements) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify the Interface, use --help for more information")
    elif not options.new_mac:
        parser.error("[-] Please specify the MAC Address, use --help for more information")
    else:
        return options

def mac_changer(interface, new_mac):

    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

def read_mac(interface):

    ifconfig_output = subprocess.check_output(['ifconfig', interface])
    mac_address_change_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_output))

    if mac_address_change_result:
        return mac_address_change_result.group(0)
    if not mac_address_change_result:
        print("[-] Unable to read the MAC Address")

intro = pyfiglet.figlet_format("MAC Changer", font="standard")
print(intro)
print("------------> MAC Changer Version 1.1 by Aditya Patil <------------")

options = get_arguements()

current_mac = read_mac(options.interface)
print("[+] Current MAC Address is " + str(current_mac))

mac_changer(options.interface, options.new_mac)

current_mac = read_mac(options.interface)

if current_mac == options.new_mac:
    print("[+] MAC Address has been successfully changed to " + current_mac)

else:
    print("[-] Failed to change the MAC Address")
    print("[*] Check the inputs or it might be an internal problem")










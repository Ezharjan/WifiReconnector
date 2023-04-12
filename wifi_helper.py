# Written by Alexander Ezharjan; 12th, April, 2023.
# Note (How to use this script):
# 1. Login to your Wifi with your password and username required first
# 2. Configure the 'wifi_name' and 'interval' in this file to yours
# 3. Run this script in console board via 'python wifi.py'
# 4. Do not close the script running console, keep it open for it will reconnect if network is off.
# This script is open source under GLP license by Alexander Ezharjan.
import time
import subprocess


wifi_name = "UM_PUBLIC_WIFI"  # name of the Wifi, eg: "UM_SECURED_WLAN_5G", "UM_SECURED_WLAN"
interval = 10  # the interval in seconds for checking the network state


def isOnline():
    pingURL = "um.edu.mo"  # for checking the network
    ret = subprocess.run("ping " + pingURL + " -n 1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = True if ret.returncode == 0 else False
    return res


def connectWifi():
    try:
        # Run the netsh command to connect to the Wi-Fi network
        subprocess.check_output(f'netsh wlan connect name="{wifi_name}"', shell=True)
        print(f"Successfully connected to {wifi_name}")
        return True
    #
    except subprocess.CalledProcessError as e:
        # If the command failed, print the error message
        print("Error:", e.output.decode())
        return False


def heartBeat():
    while True:
        time.sleep(interval)
        if(not isOnline()):
            res = connectWifi()
            print("Reconnected successfully!") if res else print("Reconnection Error!")
        # else:
        #     print("Network state is nice.")


if __name__ == "__main__":
    print("Keep this window open since it helps to reconnect when network is off!")
    heartBeat()
# Written by Alexander Ezharjan; 12th, April, 2023.

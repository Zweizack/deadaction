#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, platform, json, requests 
from time import sleep

bold = "\033[1m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
cyan = "\033[36m"
white = "\033[97m"

title = """ _______                          __                     __     __                   
|       \\                        |  \\                   |  \\   |  \\                  
| ▓▓▓▓▓▓▓\\ ______   ______   ____| ▓▓ ______   _______ _| ▓▓_   \\▓▓ ______  _______  
| ▓▓  | ▓▓/      \\ |      \\ /      ▓▓|      \\ /       \\   ▓▓ \\ |  \\/      \\|       \\ 
| ▓▓  | ▓▓  ▓▓▓▓▓▓\\ \\▓▓▓▓▓▓\\  ▓▓▓▓▓▓▓ \\▓▓▓▓▓▓\\  ▓▓▓▓▓▓▓\\▓▓▓▓▓▓ | ▓▓  ▓▓▓▓▓▓\\ ▓▓▓▓▓▓▓\\
| ▓▓  | ▓▓ ▓▓    ▓▓/      ▓▓ ▓▓  | ▓▓/      ▓▓ ▓▓       | ▓▓ __| ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓
| ▓▓__/ ▓▓ ▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓ ▓▓__| ▓▓  ▓▓▓▓▓▓▓ ▓▓_____  | ▓▓|  \\ ▓▓ ▓▓__/ ▓▓ ▓▓  | ▓▓
| ▓▓    ▓▓\\▓▓     \\\\▓▓    ▓▓\\▓▓    ▓▓\\▓▓    ▓▓\\▓▓     \\  \\▓▓  ▓▓ ▓▓\\▓▓    ▓▓ ▓▓  | ▓▓
 \\▓▓▓▓▓▓▓  \\▓▓▓▓▓▓▓ \\▓▓▓▓▓▓▓ \\▓▓▓▓▓▓▓ \\▓▓▓▓▓▓▓ \\▓▓▓▓▓▓▓   \\▓▓▓▓ \\▓▓ \\▓▓▓▓▓▓ \\▓▓   \\▓▓
"""

try:

  if (platform.system() == 'Windows'):
    os.system('cls')
  else:
    os.system('clear')

  print(bold+green+title)

  print(cyan+'-' * 0x33)
  ip = input(white+'IP: '+yellow).strip()
  print(cyan+'-' * 0x33)

  response = requests.post('https://ipinfo.io/products/proxy-vpn-detection-api', data={'input': ip}).json()
  response = json.loads(json.dumps(response))

  print(f"{white}({yellow}I. SCAN{white})\n")

  for service, result in response.items():
    if (result == True):
      color = green
    else:
      color = red
    print(f'{white}{service.upper():12}{yellow}: {color}{str(result).upper()}')

  print(cyan+'-' * 0x33)

  response = requests.get(f'https://proxycheck.io/v2/{ip}?vpn=1').json()
  response = json.loads(json.dumps(response))

  print(f"{white}({yellow}II. SCAN{white})\n")

  if(response[ip]['proxy'] == 'yes'):
    color = green
  else:
    color = red

  for service, result in response[ip].items():
    print(f'{white}{service.upper():12}{yellow}: {color}{str(result).upper()}')

  print(cyan+'-' * 0x33)

except KeyboardInterrupt:
  exit(red+"\n[!] STOP")

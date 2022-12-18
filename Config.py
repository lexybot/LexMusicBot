import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5870406957:AAEdvFwNYdsXjaukiBNiaBPdobnQR1pmIrg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIkBu75jhnHmriOUS8e2WNPJR_JoR4_g_oAoxbQxm-KcYdXWfdR0k4PTOYw79todEgoTOrX545gAJcY1GCsPFCN4FyTRhAqptGtuXygsAh8dVY2D0lswwBmTF3hHRYxkuzt-dvTsUOxizeTsh6MBm590tW0vaD3rsQYCO3AzDjsxKdsugKRS3orbf6jfApZeyQeX2j2SnvvEbsjlAjnv89Vw5uojY2Be8egnxC-Hhpwrf6aEuq_BbtwAfb8I5l1lPa_zWRA2bxYDovtoJHEHx7gpFxSwOhXxpJBF7vd8uqvPGbnrDlDGdW09kaO1W0wVq3Cs91lS_G9qD99m-PpcK86Js0E=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@lexsibot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5746950993")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional

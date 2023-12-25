class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "25488022"
    API_HASH = "0c999a454fddd79251213be7944811e8"

    CASH_API_KEY = "4ONZ97XPO2DXJ3GR"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://jzjlqwznxcrmzw:78cf804338ff548c524b0a7cf3e98e9498a74371e635f3bef9cb33b00b10f83a@ec2-35-169-184-61.compute-1.amazonaws.com:5432/dchiv1qcmt7mkt"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://vivek:vivek@vivekmusicbot.ogzyexq.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "bseb9th"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6768491785:AAG3cHOeu-2ZuOu31PKvxnx_ZqNumRxvJl4"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "0UJPW4SY5W5G"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6815918609 # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

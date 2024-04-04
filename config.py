import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21927988")

API_HASH = os.environ.get("API_HASH", "e18f720acdff1e5b0ec80616aecd8a5a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5906990280:AAExANmoPaiHklCUPHOS-WAYwFPKde2fmU8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "BotsbyChad") 

DB_NAME = os.environ.get("DB_NAME","tanya")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://dokjakim155:yDDGwCNR3SqCVuNl@telegram.a5ag6r1.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "100000"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/79aaad5da1ac1df115092.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2064735436').split()]

PORT = os.environ.get('PORT', '8080')

WEBHOOK = bool(os.environ.get("WEBHOOK", True))

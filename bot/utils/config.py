import os


class Config:
    API_ID = int(os.environ.get("API_ID", 27418440)) #GANTI "1234" DENGAN API_ID
    API_HASH: str = os.environ.get("API_HASH", "0a08a360e0e9f41b9896f655c300d09d") #GANTI "b184" DENGAN API_HASH , JANGAN HAPUS TANDA (" ") NYA !!!
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "7891755815:AAF1wYjwhPZtttnETyFrNNaYUjy4LF9tPPU") #GANTI "7u9jl" DENGAN TOKEN BOT , JANGAN HAPUS TANDA (" ") NYA !!!
    OWNER_ID = int(os.environ.get("OWNER_ID", 1927018403)) #GANTI "1234" DENGAN ID PEMILIK BOT
    MONGODB_URI: str = os.environ.get("MONGODB_URI", "mongodb+srv://wtfbruh:KontolXD#123@fsub.brzgete.mongodb.net/?retryWrites=true&w=majority&appName=fsub") #GANTI "mongodb://root:passwd@mongo" DENGAN URI MONGO , JANGAN HAPUS TANDA (" ") NYA !!!
    DATABASE_CHAT_ID = int(os.environ.get("DATABASE_CHAT_ID", -1002282009062)) #GANTI DENGAN DATABASE CHANNEL


config: "Config" = Config()
BOT_ID = config.BOT_TOKEN.split(":", 1)[0]

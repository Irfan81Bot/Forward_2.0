import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "17760082"))
    API_HASH = os.environ.get("API_HASH", "c3fc3cd44886967cf3c0e8585b5cad1c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6134421802:AAEAHW2TnPvXCV6D0x0ZITpMBH7Xq9xtp6M") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "1125671241")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://dsbotzz:786or786@cluster0.wrbdm8z.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "BQAWtSrBW0y_PRG02vTt0DsKDzdg4moU3JqgwyUIX9-w_bpRYmvFouW9qyKA8UTCNi4h-Nq6kcwz-paPutR-sSzwwG4kZZeunWmmNVTVYbNrCnJGeahPGHUo8C_XU8RR52S78x1IYC_yHkm5h7fhk_U3Ign6z57XStMbCt2gvJ1KJcvhgZBX_wvOKyiYxmEK6jo7WiZ6PXe6Kvy9iFVCyxsf3rDEjkeZ0HugM2PHPoVvm6R3CfnOUjHNOICSXLzRgahi-IuE4WrPBEmjMRqhx1kpMmoTV6TPGW9kqB9ltpAirR6TRk_lmrGTn8j_rsrbwTSPo5hzklAk5auY6hR3gOkGAAAAAT8AbysA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001751695482"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Auto_Forword_DS_Bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 28094107))

    API_HASH = os.environ.get("API_HASH", "1ff3955d2e53a2f76c1599b09e8f7dc2")

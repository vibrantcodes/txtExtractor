#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7108812913:AAH4fFpLqz6YYUlEFaJndm4Es4PjEpCJmtE")
    API_ID = int(os.environ.get("API_ID", "27544192"))
    API_HASH = os.environ.get("API_HASH", "cac44b2f15d1913816fa67293bc81311")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1124959107")

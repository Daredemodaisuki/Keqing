import json
import os

# 版本
KQS_VERSION: str = json.load(open("global_const.json", "r"))["KQS_VERSION"]
# 包名
KQS_CORE_NAME: str = json.load(open("global_const.json", "r"))["KQS_CORE_NAME"]
# 👴和刻晴小姐的结婚纪念日🥰
KQS_START_ID: int = json.load(open("global_const.json", "r"))["KQS_START_ID"]

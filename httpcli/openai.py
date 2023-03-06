"""
@Project ：WechatBot 
@File    ：openai.py
@IDE     ：PyCharm 
@Author  ：zhizhuo
@Date    ：2023/2/1 16:03 
"""
import configparser
import os

import openai

from httpcli.output import *

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, "../config/config.ini")
config = configparser.ConfigParser()  # 类实例化
config.read(config_path, encoding="utf-8")
openai_key = config.get("apiService", "openai_key")
openai.api_key = openai_key


def OpenaiServer(msg=None):
    try:
        if msg is None:
            output(f'ERROR：msg is None')
            msg = ""
        else:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "你是ChatGPT, 一个由OpenAI训练的大型语言模型, 你旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。"},
                    {"role": "user", "content": str(msg)}
                ],
                temperature=0.6,
                max_tokens=1000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            # msg = "来自openai回复结果：\n"
            msg = response.choices[0]['message']['content']
            # msg += "\n\rCreate by openai server"
    except Exception as e:
        output(f"ERROR：{e}")
        msg = e
    return msg


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
问候脚本

这个脚本用于向用户或指定的人问好。
使用方法：
1. 确保你的系统已安装Python 3
2. 在命令行中运行：python greeting.py
3. 或运行：python greeting.py [名字]，例如：python greeting.py Alice
"""

import sys
from datetime import datetime

def get_greeting_time():
    """根据当前时间获取合适的问候语前缀"""
    hour = datetime.now().hour
    if 6 <= hour < 12:
        return "早上好"
    elif 12 <= hour < 18:
        return "下午好"
    elif 18 <= hour < 22:
        return "晚上好"
    else:
        return "夜深了"

def say_hello(name="世界"):
    """向指定名称的人问好
    
    Args:
        name (str): 要问候的人的名字，默认为"世界"
    """
    time_greeting = get_greeting_time()
    print(f"{time_greeting}，{name}！")
    print(f"欢迎使用Python问候脚本！")

if __name__ == "__main__":
    # 检查是否有命令行参数
    if len(sys.argv) > 1:
        # 使用命令行参数作为名字
        name = " ".join(sys.argv[1:])
        say_hello(name)
    else:
        # 向世界问好
        say_hello()
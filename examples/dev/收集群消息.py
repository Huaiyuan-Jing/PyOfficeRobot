# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：python-office
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/8/9 23:05 
@本段代码的视频说明     ：
'''
import PyOfficeRobot as pr

pr.chat.receive_message(who='程序员晚枫', txt='userMessage.txt', output_path='/')

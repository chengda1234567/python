#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

import datetime

__author__ = 'ChengDa'

'''
python 中修饰器的用法

测试结果与预测结果 不一致 则会报错

'''

class test(object):
    ''' #执行测试只能写在顶部
    >>> cd=test()
    >>> cd.Now()
    2018-12-25
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        logging.info('用户名: %s 年龄: %s' % (self.name, self.age))

    #定义一个当前时间
    nowTime='2018-12-25'
    #修饰器会传入当前函数
    def GetTime(func):
        def wrapper(self):
            #在执行函数前执行某些方法
            #logging.info('call %s():' % func.__name__)
            self.name='dacheng'
            self.age='33'
            global nowTime
            nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logging.info('获取到当前时间 %s' % nowTime)
            return func(self)
        return wrapper

    @GetTime
    def Now(self):
        global nowTime
        print  nowTime
        logging.info('打印当前时间')
        logging.info('在赋值后 修饰符 已经修改 用户名: %s 年龄: %s' % (self.name,self.age))



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    #import doctest
    #doctest.testmod()
    cd1=test('chengda','22')
    cd1.Now();
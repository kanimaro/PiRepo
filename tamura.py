#!/usr/bin python

import re
import sys 
import datetime

SUCCESS = 0
FAILURE = -1

def KnowTime():
  dt_start = datetime.datetime(2018, 2, 1, 0,0,0,0)
  dt_end = datetime.datetime(2018, 10, 1, 0,0,0,0)
  print(dt_end - dt_start)
  return SUCCESS

if __name__ == '__main__':
    if KnowTime() == SUCCESS:
      print("OK")

# -*- coding: utf-8 -*-
'''
Created on Mar 9, 2010

@author: epeli
'''

from subssh import tools
from subssh import config


def whoami(username, cmd, args):
    tools.writeln(username)

cmds = {
        "whoami": whoami,
        }


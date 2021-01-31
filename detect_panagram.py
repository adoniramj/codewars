#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:03:23 2021

@author: ubu20
"""

import string


pangram = "abcde"
#pangram = "The quick, brown fox jumps over the lazy dog!"


def is_pangram(s):
    s = s.lower()
    str_ = ''
    for letter in s:
        if letter.isalpha():
            str_ += letter
    str_ = set(str_)
    if len(string.ascii_lowercase) == len(str_):
        return True
    else:
        return False


result = is_pangram(pangram)

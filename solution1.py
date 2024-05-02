# name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time

def name_args(**kwargs):
    for i in kwargs:
        print(i, ':', kwargs[i])

name_args(a='abc', b='def', c='ghi')
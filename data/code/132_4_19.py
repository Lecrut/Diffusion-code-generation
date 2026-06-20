negate_table = {True: False, False: True}

def negate_if_false(boolean_value):
    return negate_table[boolean_value]
if __name__ == '__main__':
    print(negate_if_false(False))
    print(negate_if_false(True))
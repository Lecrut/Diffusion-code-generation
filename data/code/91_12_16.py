bool_negation_table = {True: False, False: True}

def negate_boolean(value):
    return bool_negation_table[value]

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))
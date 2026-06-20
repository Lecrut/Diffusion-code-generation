def negate_boolean(value):
    negation_map = {True: False, False: True}
    return negation_map[value]

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))
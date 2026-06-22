def negate(value):
    table = {True: False, False: True}
    return table[value]

if __name__ == '__main__':
    print(negate(True))
    print(negate(False))
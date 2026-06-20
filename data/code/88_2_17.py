def both_true(val1, val2):
    return val1 and val2
if __name__ == '__main__':
    print(both_true(True, True))
    print(both_true(False, True))
    print(both_true(True, False))
    print(both_true(False, False))
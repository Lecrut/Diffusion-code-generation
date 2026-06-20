def both_true(a, b):
    return bool(a) and bool(b)
if __name__ == '__main__':
    print(both_true(True, True))
    print(both_true(False, True))
    print(both_true(True, False))
    print(both_true(False, False))
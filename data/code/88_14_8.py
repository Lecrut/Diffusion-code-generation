def both_true(a, b):
    return bool(a) and bool(b)

if __name__ == '__main__':
    print(both_true(True, False))
    print(both_true(0, 1))
    print(both_true('hello', 'world'))
    print(both_true(None, None))
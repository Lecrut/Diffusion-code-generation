def is_strictly_true(value):
    return bool(value)

if __name__ == '__main__':
    print(is_strictly_true(1))
    print(is_strictly_true(0))
    print(is_strictly_true('hello'))
    print(is_strictly_true(''))
    print(is_strictly_true(None))
    print(is_strictly_true(True))
    print(is_strictly_true(False))
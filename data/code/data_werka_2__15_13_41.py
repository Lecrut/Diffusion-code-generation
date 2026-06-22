def strict_equals(a, b):
    return type(a) == type(b) and a == b
if __name__ == '__main__':
    print(strict_equals(10, 10))
    print(strict_equals(10, '10'))
    print(strict_equals(3.14, 3.14))
    print(strict_equals(3.14, '3.14'))
    print(strict_equals(True, True))
    print(strict_equals(True, 1))
    print(strict_equals([], []))
    print(strict_equals([], [1]))
    print(strict_equals({}, {}))
    print(strict_equals({}, {'key': 'value'}))
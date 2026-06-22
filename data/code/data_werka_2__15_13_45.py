def strict_equals(a, b):
    return type(a) == type(b) and a == b
if __name__ == '__main__':
    print(strict_equals(10, 10))
    print(strict_equals('hello', 'hello'))
    print(strict_equals(10, '10'))
    print(strict_equals(3.14, 3.14))
    print(strict_equals([1, 2], [1, 2]))
    print(strict_equals((1, 2), (1, 2)))
    print(strict_equals({1, 2}, {1, 2}))
    print(strict_equals({'a': 1}, {'a': 1}))
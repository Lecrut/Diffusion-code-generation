def strict_equals(value1, value2):
    return type(value1) is type(value2) and value1 == value2
if __name__ == '__main__':
    print(strict_equals(5, 5))
    print(strict_equals(5, '5'))
    print(strict_equals('hello', 'hello'))
    print(strict_equals('hello', 'world'))
    print(strict_equals(3.14, 3.14))
    print(strict_equals(3.14, 2.71))
    print(strict_equals([1, 2, 3], [1, 2, 3]))
    print(strict_equals((1, 2, 3), (1, 2, 3)))
    print(strict_equals({1, 2, 3}, {1, 2, 3}))
    print(strict_equals({'a': 1}, {'a': 1}))
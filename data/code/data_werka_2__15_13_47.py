def strict_equal(value1, value2):
    return type(value1) is type(value2) and value1 == value2
if __name__ == '__main__':
    print(strict_equal(5, 5))
    print(strict_equal(5, '5'))
    print(strict_equal(3.0, 3))
    print(strict_equal(True, 1))
    print(strict_equal('hello', 'hello'))
    print(strict_equal([1, 2], [1, 2]))
    print(strict_equal((1, 2), (1, 2)))
    print(strict_equal({'a': 1}, {'a': 1}))
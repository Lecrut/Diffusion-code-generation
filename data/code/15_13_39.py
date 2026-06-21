def strict_equal(value1, value2):
    return type(value1) == type(value2) and value1 == value2
if __name__ == '__main__':
    print(strict_equal(10, 10))
    print(strict_equal(10, '10'))
    print(strict_equal(3.14, 3.14))
    print(strict_equal(3.14, 3))
    print(strict_equal('hello', 'hello'))
    print(strict_equal('hello', 'world'))
    print(strict_equal([1, 2, 3], [1, 2, 3]))
    print(strict_equal([1, 2, 3], (1, 2, 3)))
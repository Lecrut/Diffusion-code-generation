def strict_equal(a, b):
    return a == b
if __name__ == '__main__':
    print(strict_equal(42, 42))
    print(strict_equal('hello', 'hello'))
    print(strict_equal(3.14, 3.14))
    print(strict_equal(True, False))
    print(strict_equal([1, 2], [1, 2]))
    print(strict_equal((1, 2), (1, 2)))
    print(strict_equal({'a': 1}, {'a': 1}))
    print(strict_equal(42, '42'))
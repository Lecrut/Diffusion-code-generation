def strict_equal(a, b):
    return type(a) == type(b) and a == b
if __name__ == '__main__':
    print(strict_equal(10, 10))
    print(strict_equal(10, '10'))
    print(strict_equal(3.14, 3.14))
    print(strict_equal(3.14, '3.14'))
    print(strict_equal(True, 1))
    print(strict_equal([], []))
    print(strict_equal({}, {}))
    print(strict_equal([1, 2], [1, 2]))
    print(strict_equal((1, 2), (1, 2)))
    print(strict_equal({1, 2}, {1, 2}))
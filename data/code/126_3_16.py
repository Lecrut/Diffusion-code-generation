is_equal_func = lambda x, y: x == y

if __name__ == '__main__':
    print(is_equal_func(42, 42))
    print(is_equal_func('apple', 'apple'))
    print(is_equal_func([1, 2, 3], [1, 2, 3]))
    print(is_equal_func([1, 2, 3], [3, 2, 1]))
is_equal_func = lambda a, b: a == b
if __name__ == '__main__':
    print(is_equal_func(15, 15))
    print(is_equal_func('apple', 'apple'))
    print(is_equal_func([3, 4], [3, 4]))
    print(is_equal_func(20, 10))
    print(is_equal_func('banana', 'apple'))
is_equal_func = lambda a, b: a == b

if __name__ == '__main__':
    print(is_equal_func(5, 5))
    print(is_equal_func('apple', 'apple'))
    print(is_equal_func([1, 2], [1, 2]))
    print(is_equal_func(3, 4))
    print(is_equal_func('hello', 'world'))
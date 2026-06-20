is_equal_func = lambda x, y: x == y

if __name__ == '__main__':
    print(is_equal_func(15, 15))
    print(is_equal_func('world', 'world'))
    print(is_equal_func([3, 4], [3, 4]))
    print(is_equal_func({'a': 1}, {'a': 1}))
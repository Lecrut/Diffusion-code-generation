def any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    test_values = [False, False, True]
    result = any_true(test_values)
    print(result)
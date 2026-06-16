def has_positive_value(iterable):
    return any(x > 0 for x in iterable)
if __name__ == '__main__':
    test_data = [1, -2, 3, 4]
    result = has_positive_value(test_data)
    print(result)
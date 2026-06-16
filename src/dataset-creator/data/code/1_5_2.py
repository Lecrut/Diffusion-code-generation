def has_positive_value(iterable):
    return any(x > 0 for x in iterable)
if __name__ == '__main__':
    test_data = [1, -5, 3]
    print(has_positive_value(test_data))
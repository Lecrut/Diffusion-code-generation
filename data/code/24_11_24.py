def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [-10, -1, 0, 1, 10]
    results = [is_negative(v) for v in test_values]
    print(results)
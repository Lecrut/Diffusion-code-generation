def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [-1, 0, 1, -5.5, 3.2]
    results = [is_negative(val) for val in test_values]
    print(results)
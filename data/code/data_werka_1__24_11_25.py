def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [10, -5, 0, -3.5, 2.7]
    results = {val: is_negative(val) for val in test_values}
    print(results)
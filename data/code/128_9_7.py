def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [-7, 4, -1, 0, 3]
    results = {val: is_negative(val) for val in test_values}
    print(results)
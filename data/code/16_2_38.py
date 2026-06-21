def check_positive(value):
    return value > 0

if __name__ == '__main__':
    test_values = [7, -2, 0]
    for val in test_values:
        result = check_positive(val)
        print(result)
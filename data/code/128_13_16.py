def is_negative(num):
    return num < 0

if __name__ == '__main__':
    test_values = [-10, 5, -0.5, 0, 2]
    results = [is_negative(val) for val in test_values]
    print(results)
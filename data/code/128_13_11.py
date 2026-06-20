def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [-5, -1.5, 0, 3]
    results = [is_negative(x) for x in test_values]
    print(results)
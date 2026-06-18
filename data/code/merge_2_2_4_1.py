def is_positive(value):
    return value > 0
if __name__ == '__main__':
    test_values = [-5, -1, 0, 1, 2]
    results = [is_positive(v) for v in test_values]
    print(results)
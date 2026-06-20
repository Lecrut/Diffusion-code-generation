def check_conditions(value):
    return value > 0 or value == 10

if __name__ == '__main__':
    test_values = [5, -3, 10, 0]
    results = [check_conditions(v) for v in test_values]
    print(results)
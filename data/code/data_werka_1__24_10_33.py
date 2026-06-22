is_negative = lambda x: x < 0

if __name__ == '__main__':
    test_values = [10, -5, 0, -3, 7]
    results = [is_negative(value) for value in test_values]
    print(results)
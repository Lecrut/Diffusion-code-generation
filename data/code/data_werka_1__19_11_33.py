def is_positive(number):
    return number > 0

if __name__ == '__main__':
    test_values = [10, -5, 0, 23, -1]
    results = [is_positive(value) for value in test_values]
    print(results)
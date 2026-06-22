def is_positive(number):
    return number > 0

if __name__ == '__main__':
    test_values = [5, -3, 0, 2.7, -1.5]
    results = [is_positive(value) for value in test_values]
    print(results)
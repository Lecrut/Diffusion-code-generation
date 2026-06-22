def is_positive(number):
    return number > 0

if __name__ == '__main__':
    test_cases = [-10, 0, 5, -3.14, 7.2]
    results = {value: is_positive(value) for value in test_cases}
    print(results)
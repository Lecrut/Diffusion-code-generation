def is_positive(number):
    return number > 0

if __name__ == '__main__':
    TEST_VALUES = [0, -1, 2.5, -3.6, 100]
    results = {value: is_positive(value) for value in TEST_VALUES}
    print(results)
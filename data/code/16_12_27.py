def is_positive(number):
    return number > 0

if __name__ == '__main__':
    test_values = [-10, -1, 0, 0.5, 100]
    for value in test_values:
        print(is_positive(value))
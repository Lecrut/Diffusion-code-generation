def is_positive(number):
    try:
        return int(number) > 0
    except ValueError:
        return False

if __name__ == '__main__':
    test_values = [10, -5, 'abc', 0, 23]
    for value in test_values:
        print(is_positive(value))
def is_positive(number):
    return isinstance(number, (int, float)) and number > 0

if __name__ == '__main__':
    test_values = [10, -5, 0, 3.14, -2.71, 'hello', None]
    for value in test_values:
        print(f"{value}: {is_positive(value)}")
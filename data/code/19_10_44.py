def is_positive(number):
    return number > 0

if __name__ == '__main__':
    test_values = [25, -10, 0, 7, -3]
    for value in test_values:
        result = is_positive(value)
        print(f"is_positive({value}) = {result}")
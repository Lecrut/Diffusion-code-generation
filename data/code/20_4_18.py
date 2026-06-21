def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, 45, 100, -3, -4]
    for value in test_values:
        result = is_even(value)
        print(f"is_even({value}) returns {result}")
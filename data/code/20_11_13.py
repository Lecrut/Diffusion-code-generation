def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [0, 2, -2, 5, -5, 100, -100, 1]
    for value in test_values:
        result = is_even(value)
        print(f"is_even({value}) returned {result}")
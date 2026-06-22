def sum_of_digits(number):
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

if __name__ == '__main__':
    test_values = [0, 5, 123, 9999]
    for val in test_values:
        result = sum_of_digits(val)
        print(result)
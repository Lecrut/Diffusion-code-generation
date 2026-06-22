def sum_of_digits(n: int) -> int:
    number = abs(n)
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

if __name__ == '__main__':
    test_values = [12345, -9876, 0, 50000, -1]
    for value in test_values:
        result = sum_of_digits(value)
        print(result)
def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

if __name__ == '__main__':
    test_values = [0, 7, 42, 12345, 99999]
    for value in test_values:
        result = sum_of_digits(value)
        print(f"Sum of digits of {value}: {result}")
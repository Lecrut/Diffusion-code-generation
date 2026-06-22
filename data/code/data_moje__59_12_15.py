def sum_digits_recursive(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_digits_recursive(n // 10)

if __name__ == '__main__':
    sample_values = [123, 456, 7890, 99, 5, 12345]
    for val in sample_values:
        result = sum_digits_recursive(val)
        print(result)
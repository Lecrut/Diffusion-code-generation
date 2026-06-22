def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total

if __name__ == '__main__':
    sample_values = [0, 123, 9999, 50005]
    for value in sample_values:
        result = sum_of_digits(value)
        print(result)
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    sample_values = [12345, 0, 999, 10001]
    for val in sample_values:
        print(sum_digits(val))
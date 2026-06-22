def sum_digits(number: int) -> int:
    n = abs(number)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    sample_number = 98765432101234567890
    result = sum_digits(sample_number)
    print(result)
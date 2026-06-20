def divide_large_integers(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

if __name__ == '__main__':
    sample_dividend = 12345678901234567890
    sample_divisor = 987654321
    result = divide_large_integers(sample_dividend, sample_divisor)
    print(result)
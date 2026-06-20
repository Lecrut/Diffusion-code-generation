def divide_large_integers(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

if __name__ == '__main__':
    result = divide_large_integers(12345678901234567890, 987654321)
    print(result)
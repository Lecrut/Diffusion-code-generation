def optimized_division(dividend, divisor):
    return dividend // divisor
if __name__ == '__main__':
    large_dividend = 12345678901234567890
    divisor = 12345
    result = optimized_division(large_dividend, divisor)
    print(result)
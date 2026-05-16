def optimized_division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Division by zero")
    return dividend // divisor
if __name__ == '__main__':
    dividend_large = 12345678901234567890
    divisor_small = 12345
    result = optimized_division(dividend_large, divisor_small)
    print(result)
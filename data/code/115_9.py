def optimized_division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return dividend // divisor
if __name__ == '__main__':
    large_number = 12345678901234567890
    divisor = 12345
    result = optimized_division(large_number, divisor)
    print(result)
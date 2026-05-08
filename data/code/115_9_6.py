import sys
def large_integer_division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Division by zero")
    return dividend // divisor
if __name__ == '__main__':
    dividend = 12345678901234567890
    divisor = 9876543210
    result = large_integer_division(dividend, divisor)
    print(result)
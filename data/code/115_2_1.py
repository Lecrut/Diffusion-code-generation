import math
def optimized_division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return float(dividend) / float(divisor)
if __name__ == '__main__':
    dividend_val = 10
    divisor_val = 3
    result = optimized_division(dividend_val, divisor_val)
    print(result)
    dividend_val = 10
    divisor_val = 2
    result = optimized_division(dividend_val, divisor_val)
    print(result)
    dividend_val = 7
    divisor_val = 2
    result = optimized_division(dividend_val, divisor_val)
    print(result)
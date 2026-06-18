def multiply_and_divide(dividend, divisor):
    try:
        result_division = dividend / divisor
        result_multiplication = dividend * divisor
        return result_multiplication, result_division
    except ZeroDivisionError:
        return "Error: Division by zero", None
if __name__ == '__main__':
    dividend_val = 10
    divisor_val = 2
    result = multiply_and_divide(dividend_val, divisor_val)
    print(f"Dividend: {dividend_val}, Divisor: {divisor_val}")
    print(f"Multiplication Result: {result[0]}")
    print(f"Division Result: {result[1]}")
    dividend_val = 10
    divisor_val = 0
    result = multiply_and_divide(dividend_val, divisor_val)
    print(f"\nDividend: {dividend_val}, Divisor: {divisor_val}")
    print(f"Result: {result}")
    dividend_val = 15
    divisor_val = -3
    result = multiply_and_divide(dividend_val, divisor_val)
    print(f"\nDividend: {dividend_val}, Divisor: {divisor_val}")
    print(f"Multiplication Result: {result[0]}")
    print(f"Division Result: {result[1]}")
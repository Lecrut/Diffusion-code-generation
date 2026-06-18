def multiply_and_divide(dividend, divisor):
    if divisor == 0:
        return "Error: Division by zero"
    result_multiplication = dividend * divisor
    result_division = dividend / divisor
    return result_multiplication, result_division
if __name__ == '__main__':
    dividend_val = 10
    divisor_val = 2
    result = multiply_and_divide(dividend_val, divisor_val)
    print(f"Dividend: {dividend_val}, Divisor: {divisor_val}")
    print(f"Multiplication result: {result[0]}")
    print(f"Division result: {result[1]}")
    dividend_val = 10
    divisor_val = 0
    result_error = multiply_and_divide(dividend_val, divisor_val)
    print(f"\nDividend: {dividend_val}, Divisor: {divisor_val}")
    print(f"Result: {result_error}")
    dividend_val = 15
    divisor_val = -3
    result_neg = multiply_and_divide(dividend_val, divisor_val)
    print(f"\nDividend: {dividend_val}, Divisor: {divisor_val}")
    print(f"Multiplication result: {result_neg[0]}")
    print(f"Division result: {result_neg[1]}")
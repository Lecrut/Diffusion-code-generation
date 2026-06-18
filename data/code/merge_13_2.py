def calculate_division(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder
if __name__ == '__main__':
    dividend_value = 25
    divisor_value = 4
    quotient_result, remainder_result = calculate_division(dividend_value, divisor_value)
    print(f"Dividend: {dividend_value}")
    print(f"Divisor: {divisor_value}")
    print(f"Quotient: {quotient_result}")
    print(f"Remainder: {remainder_result}")
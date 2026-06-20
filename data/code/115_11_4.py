def calculate_division_and_modulo(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

if __name__ == '__main__':
    num1 = 100
    num2 = 7
    try:
        result_quotient, result_remainder = calculate_division_and_modulo(num1, num2)
        print(f"Quotient of {num1} // {num2}: {result_quotient}")
        print(f"Remainder of {num1} % {num2}: {result_remainder}")
    except ValueError as e:
        print(f"Error: {e}")
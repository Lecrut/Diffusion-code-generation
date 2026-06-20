def perform_division_and_modulus(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

if __name__ == '__main__':
    num1 = 100
    num2 = 7
    result_quotient, result_remainder = perform_division_and_modulus(num1, num2)
    print(f"Quotient of {num1} // {num2}: {result_quotient}")
    print(f"Remainder of {num1} % {num2}: {result_remainder}")
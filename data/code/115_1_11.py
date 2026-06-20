def validate_division(dividend, divisor):
    if not isinstance(dividend, int) or not isinstance(divisor, int):
        raise ValueError("Both dividend and divisor must be integers.")
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")

def divide_two_numbers(dividend, divisor):
    validate_division(dividend, divisor)
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

if __name__ == '__main__':
    num1, num2 = 10, 3
    result1 = divide_two_numbers(num1, num2)
    print(f"Quotient of {num1} / {num2}: {result1[0]}, Remainder: {result1[1]}")
    
    num3, num4 = -25, 4
    result2 = divide_two_numbers(num3, num4)
    print(f"Quotient of {num3} / {num4}: {result2[0]}, Remainder: {result2[1]}")
    
    num5, num6 = 0, 7
    result3 = divide_two_numbers(num5, num6)
    print(f"Quotient of {num5} / {num6}: {result3[0]}, Remainder: {result3[1]}")
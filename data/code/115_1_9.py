def divide_two_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    quotient = a // b
    remainder = a % b
    return quotient, remainder

if __name__ == '__main__':
    num1, num2 = 15, 3
    result = divide_two_numbers(num1, num2)
    print(f"Quotient of {num1} / {num2}: {result[0]}, Remainder: {result[1]}")
    
    num3, num4 = 7, 2
    result = divide_two_numbers(num3, num4)
    print(f"Quotient of {num3} / {num4}: {result[0]}, Remainder: {result[1]}")
    
    num5, num6 = -18, 4
    result = divide_two_numbers(num5, num6)
    print(f"Quotient of {num5} / {num6}: {result[0]}, Remainder: {result[1]}")
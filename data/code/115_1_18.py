def divide_two_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    quotient = a // b
    remainder = a % b
    return quotient, remainder

if __name__ == '__main__':
    num1, num2 = 10, 3
    result1 = divide_two_numbers(num1, num2)
    print(f"Quotient of {num1} / {num2}: {result1[0]}, Remainder: {result1[1]}")
    
    num3, num4 = -15, 4
    result2 = divide_two_numbers(num3, num4)
    print(f"Quotient of {num3} / {num4}: {result2[0]}, Remainder: {result2[1]}")
    
    num5, num6 = 20, 0
    try:
        result3 = divide_two_numbers(num5, num6)
    except ZeroDivisionError as e:
        print(e)
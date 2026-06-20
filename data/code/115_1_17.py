def divide_two_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    quotient = a // b
    remainder = a % b
    return quotient, remainder

if __name__ == '__main__':
    num1 = 25
    num2 = 4
    result1 = divide_two_numbers(num1, num2)
    print(f"Quotient of {num1} / {num2}: {result1[0]}, Remainder: {result1[1]}")
    
    num3 = -18
    num4 = 5
    result2 = divide_two_numbers(num3, num4)
    print(f"Quotient of {num3} / {num4}: {result2[0]}, Remainder: {result2[1]}")
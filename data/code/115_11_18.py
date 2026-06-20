def perform_division_and_modulus(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    quotient = a // b
    remainder = a % b
    return quotient, remainder

if __name__ == '__main__':
    num1 = 100
    num2 = 7
    try:
        quotient, remainder = perform_division_and_modulus(num1, num2)
        print(f"Quotient of {num1} // {num2}: {quotient}")
        print(f"Remainder of {num1} % {num2}: {remainder}")
    except ValueError as e:
        print(f"Error: {e}")
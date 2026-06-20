def safe_division(numerator, denominator):
    try:
        quotient = numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return quotient

if __name__ == '__main__':
    num1 = 20.5
    num2 = 4.2
    result = safe_division(num1, num2)
    if result is not None:
        print(result)
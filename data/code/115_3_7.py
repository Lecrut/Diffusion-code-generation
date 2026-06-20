def divide(numerator, denominator):
    if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
        raise TypeError("Both inputs must be numeric.")
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return numerator / denominator

if __name__ == '__main__':
    num1 = 25
    num2 = 5
    result = divide(num1, num2)
    print(f"Result of {num1} divided by {num2}: {result}")
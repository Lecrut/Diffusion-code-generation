def calculate_division(numerator, denominator):
    if denominator == 0:
        return "Error: Cannot divide by zero."
    else:
        return numerator / denominator
if __name__ == '__main__':
    num1 = 20
    num2 = 4
    result = calculate_division(num1, num2)
    print(f"The result of dividing {num1} by {num2} is: {result}")
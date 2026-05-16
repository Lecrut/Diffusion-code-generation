def multiply_numbers(a, b):
    return a * b
if __name__ == '__main__':
    num1 = 15
    num2 = 7
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        result = multiply_numbers(num1, num2)
        print(result)
    else:
        print("Error: Both inputs must be valid numbers.")
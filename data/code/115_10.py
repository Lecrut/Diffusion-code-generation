def calculate_division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2
if __name__ == '__main__':
    num1 = 10
    num2 = 2
    result = calculate_division(num1, num2)
    print(result)
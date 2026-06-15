def calculator():
    num1 = 20
    num2 = 5
    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Division:", "Error: Cannot divide by zero")
if __name__ == '__main__':
    calculator()
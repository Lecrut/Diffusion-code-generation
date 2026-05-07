def calculate(num1, num2, symbol):
    if symbol == '+':
        return num1 + num2
    elif symbol == '-':
        return num1 - num2
    elif symbol == '*':
        return num1 * num2
    elif symbol == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    operator = '*'
    result = calculate(num1, num2, operator)
    print(f"Result: {result}")
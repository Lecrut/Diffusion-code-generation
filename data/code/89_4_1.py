def evaluate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            raise ZeroDivisionError("Cannot divide by zero")
    else:
        raise ValueError(f"Unsupported operator: {operator}")
OPERATORS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}
if __name__ == '__main__':
    a = 10
    b = 5
    operators_to_test = ['+', '-', '*', '/']
    for op in operators_to_test:
        if op in OPERATORS:
            result = OPERATORS[op](a, b)
            print(f"{a} {op} {b} = {result}")
        else:
            print(f"Operator {op} is not supported.")
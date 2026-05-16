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
    numbers1 = 20
    numbers2 = 5
    operators_to_test = ['+', '-', '*', '/']
    for op in operators_to_test:
        if op in OPERATORS:
            result = OPERATORS[op](numbers1, numbers2)
            print(f"{numbers1} {op} {numbers2} = {result}")
        else:
            print(f"Operator {op} is not supported.")
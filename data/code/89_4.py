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
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            raise ZeroDivisionError("Cannot perform modulo by zero")
    else:
        raise ValueError(f"Unsupported operator: {operator}")
OPERATORS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '%': lambda a, b: a % b
}
if __name__ == '__main__':
    num_a = 20
    num_b = 5
    operators_to_test = ['+', '-', '*', '/', '%']
    for op in operators_to_test:
        if op in OPERATORS:
            result = OPERATORS[op](num_a, num_b)
            print(f"{num_a} {op} {num_b} = {result}")
        else:
            print(f"Operator {op} is not supported.")
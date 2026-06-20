def parse_expression(expression):
    tokens = expression.split()
    if len(tokens) != 3:
        raise ValueError("Invalid input format")
    return tokens

def validate_operands(num1, num2):
    try:
        float(num1)
        float(num2)
    except ValueError:
        raise ValueError("Both operands must be numbers")

def evaluate_operation(num1, operator, num2):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else float('inf')
    }
    if operator not in operations:
        raise ValueError("Unsupported operator")
    return operations[operator](float(num1), float(num2))

def evaluate_expression(expression):
    tokens = parse_expression(expression)
    num1, operator, num2 = tokens
    validate_operands(num1, num2)
    return evaluate_operation(num1, operator, num2)

if __name__ == '__main__':
    try:
        result = evaluate_expression('10 / 2')
        print(result)
    except ValueError as e:
        print(e)
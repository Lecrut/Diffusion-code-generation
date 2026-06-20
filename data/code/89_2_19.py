def parse_expression(expression):
    tokens = expression.split()
    if len(tokens) != 3:
        raise ValueError("Invalid input format")
    num1, operator, num2 = tokens
    return num1, operator, num2

def convert_to_float(num_str):
    try:
        return float(num_str)
    except ValueError:
        raise ValueError("Operand must be a number")

def evaluate_operation(num1, operator, num2):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else float('inf')
    }
    if operator not in operations:
        raise ValueError("Unsupported operator")
    return operations[operator](num1, num2)

def evaluate_expression(expression):
    num1_str, operator, num2_str = parse_expression(expression)
    num1 = convert_to_float(num1_str)
    num2 = convert_to_float(num2_str)
    result = evaluate_operation(num1, operator, num2)
    return result

if __name__ == '__main__':
    try:
        result = evaluate_expression('3 / 0')
        print(result)
    except ValueError as e:
        print(e)
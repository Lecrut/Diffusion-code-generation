def validate_expression(num1, num2, operator):
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise ValueError("Numbers must be integers or floats")
    if operator not in ('+', '-', '*', '/'):
        raise ValueError("Invalid operator. Use '+', '-', '*', '/'")

def evaluate_expression(num1, num2, operator):
    validate_expression(num1, num2, operator)
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Error: Division by zero")
        else:
            return num1 / num2

if __name__ == '__main__':
    sample_numbers = [10, 5, 2, 0, -3]
    sample_operators = ['+', '-', '*', '/']
    result = evaluate_expression(sample_numbers[0], sample_numbers[1], sample_operators[0])
    print(result)
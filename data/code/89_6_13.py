def validate_numbers(numbers):
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All elements must be numbers")
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required")

def apply_operator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        return num1 / num2
    else:
        raise ValueError("Invalid operator")

def evaluate_expression(numbers, operators):
    validate_numbers(numbers)
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = apply_operator(result, numbers[i], operators[i-1])
    return result

if __name__ == '__main__':
    sample_numbers = [10, 5, 2, 0, -3]
    sample_operators = ['+', '-', '*', '/']
    print(evaluate_expression(sample_numbers, sample_operators))
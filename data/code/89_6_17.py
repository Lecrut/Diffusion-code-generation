def evaluate_expression(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError("Invalid operator entered.")

def evaluate_sequence(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        result = evaluate_expression(result, numbers[i + 1], operators[i])
    return result

if __name__ == '__main__':
    sample_numbers = [10, 5, 2, 0, -3, 100]
    sample_operators = ['+', '-', '*', '/']
    print(evaluate_sequence(sample_numbers, sample_operators))
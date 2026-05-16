import random
def evaluate_expression(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"
if __name__ == '__main__':
    sample_numbers = [10, 5, 2, 0, -3]
    sample_operators = ['+', '-', '*', '/']
    for _ in range(5):
        num1 = random.choice(sample_numbers)
        num2 = random.choice(sample_numbers)
        operator = random.choice(sample_operators)
        result = evaluate_expression(num1, operator, num2)
        print(f"Numbers: {num1}, {num2}, Operator: {operator}")
        print(f"Result: {result}")
        print("-" * 20)
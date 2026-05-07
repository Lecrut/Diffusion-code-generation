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
            raise ValueError("Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError("Invalid operator entered.")
if __name__ == '__main__':
    sample_numbers = [10, 5, 2, 0, -3, 100]
    sample_operators = ['+', '-', '*', '/']
    for _ in range(5):
        num1 = random.choice(sample_numbers)
        num2 = random.choice(sample_numbers)
        operator = random.choice(sample_operators)
        try:
            result = evaluate_expression(num1, operator, num2)
            print(f"Numbers: {num1}, {num2}, Operator: {operator}")
            print(f"Result: {num1} {operator} {num2} = {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")
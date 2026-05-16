def evaluate_fully_parenthesized(expression):
    if not expression:
        return None
    if expression.startswith('(') and expression.endswith(')'):
        content = expression[1:-1]
        balance = 0
        split_index = -1
        for i, char in enumerate(content):
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance == 0:
                split_index = i + 1
                break
        if split_index != -1:
            left = content[:split_index]
            right = content[split_index:]
            left_val = evaluate_fully_parenthesized(left)
            right_val = evaluate_fully_parenthesized(right)
            if left_val is not None and right_val is not None:
                if expression.startswith('(') and expression.endswith(')'):
                    return eval(f"{left_val} {right_val}")
    return None
def parse_and_evaluate(expression):
    if not expression:
        return None
    expression = expression.strip()
    if not expression:
        return None
    if expression.startswith('(') and expression.endswith(')'):
        content = expression[1:-1]
        balance = 0
        split_index = -1
        for i, char in enumerate(content):
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance == 0:
                split_index = i + 1
                break
        if split_index != -1:
            left = content[:split_index]
            right = content[split_index:]
            left_val = parse_and_evaluate(left)
            right_val = parse_and_evaluate(right)
            if left_val is not None and right_val is not None:
                return eval(f"{left_val} {right_val}")
    return None
def calculate_expression(expression):
    return parse_and_evaluate(expression)
if __name__ == '__main__':
    expression1 = "((1 + 2) * (3 - 4))"
    result1 = calculate_expression(expression1)
    print(f"Expression: {expression1}, Result: {result1}")
    expression2 = "((10 - (5 + 2)) * 3)"
    result2 = calculate_expression(expression2)
    print(f"Expression: {expression2}, Result: {result2}")
    expression3 = "((2 + (3 * (4 - 1))) / 5)"
    result3 = calculate_expression(expression3)
    print(f"Expression: {expression3}, Result: {result3}")
    expression4 = "((1 + (2 * (3 + 4))) / 2)"
    result4 = calculate_expression(expression4)
    print(f"Expression: {expression4}, Result: {result4}")
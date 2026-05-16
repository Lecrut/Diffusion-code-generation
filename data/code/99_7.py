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
            left_expr = content[:split_index]
            right_expr = content[split_index:]
            left_val = evaluate_fully_parenthesized(left_expr)
            right_val = evaluate_fully_parenthesized(right_expr)
            if left_val is not None and right_val is not None:
                if expression.startswith('(') and expression.endswith(')'):
                    if expression.count('(') == expression.count(')'):
                        if expression.count('(') == 1 and expression.count(')') == 1:
                            try:
                                return float(expression)
                            except ValueError:
                                return None
                        balance = 0
                        op_index = -1
                        for i in range(1, len(expression) - 1):
                            char = expression[i]
                            if char == '(':
                                balance += 1
                            elif char == ')':
                                balance -= 1
                            elif balance == 0:
                                if char in '+-*/':
                                    op_index = i
                                    break
                        if op_index != -1:
                            op = expression[op_index]
                            left_part = expression[:op_index]
                            right_part = expression[op_index+1:-1]
                            left_val = evaluate_fully_parenthesized(left_part)
                            right_val = evaluate_fully_parenthesized(right_part)
                            if left_val is not None and right_val is not None:
                                if op == '+':
                                    return left_val + right_val
                                elif op == '-':
                                    return left_val - right_val
                                elif op == '*':
                                    return left_val * right_val
                                elif op == '/':
                                    if right_val == 0:
                                        return "Error: Division by zero"
                                    return left_val / right_val
    return None
def parse_and_evaluate(expression):
    if not expression.startswith('(') or not expression.endswith(')'):
        return None
    content = expression[1:-1]
    balance = 0
    split_index = -1
    operator = None
    for i, char in enumerate(content):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        elif balance == 0:
            if char in '+-*/':
                split_index = i
                operator = char
                break
    if split_index != -1:
        left_expr = expression[1:split_index]
        right_expr = expression[split_index+1:-1]
        left_val = evaluate_fully_parenthesized(left_expr)
        right_val = evaluate_fully_parenthesized(right_expr)
        if left_val is not None and right_val is not None:
            if operator == '+':
                return left_val + right_val
            elif operator == '-':
                return left_val - right_val
            elif operator == '*':
                return left_val * right_val
            elif operator == '/':
                if right_val == 0:
                    return "Error: Division by zero"
                return left_val / right_val
    if expression.count('(') == 1 and expression.count(')') == 1:
        try:
            return float(expression)
        except ValueError:
            return None
    return None
if __name__ == '__main__':
    test_cases = [
        ("((1+2)*3)", 9.0),
        ("((10-4)/(2+1))", 2.0),
        ("((5* (2+3)) / 4)", 5.0),
        ("(10+2)*(5-3)", 24.0),
        ("(100)", 100.0),
        ("(1.5+2.5)", 4.0),
        ("((10/2)*3)", 15.0),
        ("(10/0)", "Error: Division by zero")
    ]
    for expression, expected in test_cases:
        result = parse_and_evaluate(expression)
        print(f"Expression: {expression}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print("-" * 20)
    print("Test complete.")
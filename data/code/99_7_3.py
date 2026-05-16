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
                                return float(expression[1:-1])
                            except ValueError:
                                return None
                        else:
                            balance = 0
                            op_index = -1
                            for i, char in enumerate(content):
                                if char == '(':
                                    balance += 1
                                elif char == ')':
                                    balance -= 1
                                elif balance == 0 and char in '+-*/':
                                    op_index = i
                                    break
                            if op_index != -1:
                                op = content[op_index]
                                left_str = content[:op_index]
                                right_str = content[op_index+1:]
                                left_val = evaluate_fully_parenthesized(left_str)
                                right_val = evaluate_fully_parenthesized(right_str)
                                if left_val is not None and right_val is not None:
                                    if op == '+':
                                        return left_val + right_val
                                    elif op == '-':
                                        return left_val - right_val
                                    elif op == '*':
                                        return left_val * right_val
                                    elif op == '/':
                                        if right_val == 0:
                                            raise ZeroDivisionError("Division by zero")
                                        return left_val / right_val
                            return None
        else:
            return None
    try:
        return float(expression)
    except ValueError:
        return None
def evaluate_fully_parenthesized_recursive(expression):
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
            left_str = content[:split_index]
            right_str = content[split_index:]
            left_val = evaluate_fully_parenthesized_recursive(left_str)
            right_val = evaluate_fully_parenthesized_recursive(right_str)
            if left_val is not None and right_val is not None:
                balance = 0
                op_index = -1
                for i, char in enumerate(content):
                    if char == '(':
                        balance += 1
                    elif char == ')':
                        balance -= 1
                    elif balance == 0 and char in '+-*/':
                        op_index = i
                        break
                if op_index != -1:
                    op = content[op_index]
                    left_str = content[:op_index]
                    right_str = content[op_index+1:]
                    left_val = evaluate_fully_parenthesized_recursive(left_str)
                    right_val = evaluate_fully_parenthesized_recursive(right_str)
                    if left_val is not None and right_val is not None:
                        if op == '+':
                            return left_val + right_val
                        elif op == '-':
                            return left_val - right_val
                        elif op == '*':
                            return left_val * right_val
                        elif op == '/':
                            if right_val == 0:
                                raise ZeroDivisionError("Division by zero")
                            return left_val / right_val
    try:
        return float(expression)
    except ValueError:
        return None
def calculate_expression(expression):
    return evaluate_fully_parenthesized_recursive(expression)
if __name__ == '__main__':
    test_cases = [
        "((1+2)*3)",
        "((10-5)/2)",
        "(10*(2+3))",
        "((5+5)*2)",
        "(100/5-1)",
        "((2*3)+(4*5))"
    ]
    for expr in test_cases:
        try:
            result = calculate_expression(expr)
            print(f"Expression: {expr}, Result: {result}")
        except ZeroDivisionError as e:
            print(f"Expression: {expr}, Error: {e}")
        except Exception as e:
            print(f"Expression: {expr}, Error: {e}")
        print("-" * 20)
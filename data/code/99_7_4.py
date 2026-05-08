def evaluate_fully_parenthesized(expression):
    if not expression:
        return None
    if len(expression) == 1 and expression.isdigit():
        return int(expression)
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
                    return left_val + right_val
    return None
if __name__ == '__main__':
    expression1 = "((3+4)*5)"
    expression2 = "((10-2)*(6/3))"
    expression3 = "((7+8)*(9-1))"
    expression4 = "(1+2)*(3+4)"
    expression5 = "(100)"
    print(f"Expression: {expression1}, Result: {evaluate_fully_parenthesized(expression1)}")
    print(f"Expression: {expression2}, Result: {evaluate_fully_parenthesized(expression2)}")
    print(f"Expression: {expression3}, Result: {evaluate_fully_parenthesized(expression3)}")
    print(f"Expression: {expression4}, Result: {evaluate_fully_parenthesized(expression4)}")
    print(f"Expression: {expression5}, Result: {evaluate_fully_parenthesized(expression5)}")
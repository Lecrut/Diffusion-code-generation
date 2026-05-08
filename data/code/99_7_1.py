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
            else:
                if balance == 0:
                    split_index = i
                    break
        if split_index != -1:
            left_expr = content[:split_index]
            right_expr = content[split_index+1:]
            left_val = evaluate_fully_parenthesized(left_expr)
            right_val = evaluate_fully_parenthesized(right_expr)
            if left_val is not None and right_val is not None:
                if expression[0] == '(':
                    return f"({left_val} {right_val})"
                else:
                    return left_val + right_val
    return None
def parse_and_evaluate(expression):
    result = evaluate_fully_parenthesized(expression)
    if result is not None:
        return result
    return "Error"
if __name__ == '__main__':
    expression1 = "((1 + 2) * (3 - 4))"
    expression2 = "((5 * (6 + 7)) / 2)"
    expression3 = "(10 + (20 * (3 + 4)))"
    expression4 = "(1 + 2)"
    expression5 = "(10)"
    print(f"Expression: {expression1}, Result: {parse_and_evaluate(expression1)}")
    print(f"Expression: {expression2}, Result: {parse_and_evaluate(expression2)}")
    print(f"Expression: {expression3}, Result: {parse_and_evaluate(expression3)}")
    print(f"Expression: {expression4}, Result: {parse_and_evaluate(expression4)}")
    print(f"Expression: {expression5}, Result: {parse_and_evaluate(expression5)}")
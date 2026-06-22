def evaluate_parenthesized_expression(expression: str) -> float:
    expression = expression.strip()
    if not expression:
        raise ValueError("Empty expression")
    if expression.startswith('(') and expression.endswith(')'):
        inner = expression[1:-1]
        depth = 0
        split_index = -1
        i = 0
        while i < len(inner):
            char = inner[i]
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            elif depth == 0 and char in '+-':
                split_index = i
                last_sign = char
            i += 1
        if split_index != -1:
            left = inner[:split_index]
            right = inner[split_index + 1:]
            val_left = evaluate_parenthesized_expression(left)
            val_right = evaluate_parenthesized_expression(right)
            if last_sign == '+':
                return val_left + val_right
            else:
                return val_left - val_right
        depth = 0
        split_index = -1
        i = 0
        while i < len(inner):
            char = inner[i]
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            elif depth == 0 and char in '*/':
                split_index = i
                last_op = char
            i += 1
        if split_index != -1:
            left = inner[:split_index]
            right = inner[split_index + 1:]
            val_left = evaluate_parenthesized_expression(left)
            val_right = evaluate_parenthesized_expression(right)
            if last_op == '*':
                return val_left * val_right
            else:
                return val_left / val_right
        return float(expression)
    return float(expression)

if __name__ == '__main__':
    print(evaluate_parenthesized_expression("((10 + 5) * (3 - 1))"))
    print(evaluate_parenthesized_expression("(2.5 + 3.5)"))
    print(evaluate_parenthesized_expression("((100 / 10) + 5)"))
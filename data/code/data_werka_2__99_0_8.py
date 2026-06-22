def evaluate_expression(expression: str) -> float:
    def parse_expr(pos):
        left, pos = parse_term(pos)
        while pos < len(expression) and expression[pos] in ('+', '-'):
            op = expression[pos]
            pos += 1
            right, pos = parse_term(pos)
            if op == '+':
                left = left + right
            else:
                left = left - right
        return left, pos

    def parse_term(pos):
        left, pos = parse_factor(pos)
        while pos < len(expression) and expression[pos] in ('*', '/'):
            op = expression[pos]
            pos += 1
            right, pos = parse_factor(pos)
            if op == '*':
                left = left * right
            else:
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                left = left / right
        return left, pos

    def parse_factor(pos):
        if pos >= len(expression):
            raise ValueError("Unexpected end of expression")
        char = expression[pos]
        if char == '(':
            pos += 1
            result, pos = parse_expr(pos)
            if pos >= len(expression) or expression[pos] != ')':
                raise ValueError("Missing closing parenthesis")
            pos += 1
            return result, pos
        if char == '-':
            pos += 1
            val, pos = parse_factor(pos)
            return -val, pos
        if char == '+':
            pos += 1
            val, pos = parse_factor(pos)
            return val, pos
        if char.isdigit() or char == '.':
            start = pos
            while pos < len(expression) and (expression[pos].isdigit() or expression[pos] == '.'):
                pos += 1
            num_str = expression[start:pos]
            if num_str.count('.') > 1:
                raise ValueError(f"Invalid number format: {num_str}")
            if '.' in num_str:
                return float(num_str), pos
            return int(num_str), pos
        raise ValueError(f"Unexpected character: {char}")

    pos = 0
    result, pos = parse_expr(pos)
    while pos < len(expression) and expression[pos] == ' ':
        pos += 1
    if pos < len(expression):
        raise ValueError(f"Unexpected character at end: {expression[pos:]}")
    return result

if __name__ == '__main__':
    samples = [
        "3 + 4 * 2 / ( 1 - 5 ) ^ 2",
        "10 - 2 * 3",
        "(1 + 2) * (3 + 4)",
        "100 / 10",
        "5",
        "-5 + 10",
        "((2 + 3) * 4)"
    ]
    for expr in samples:
        try:
            res = evaluate_expression(expr)
            print(f"{expr} = {res}")
        except Exception as e:
            print(f"{expr} -> Error: {e}")
def evaluate_expression(expression: str) -> float:
    def parse_expression(pos):
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
                    raise ValueError("Division by zero")
                left = left / right
        return left, pos

    def parse_factor(pos):
        if pos < len(expression) and expression[pos] == '(':
            pos += 1
            value, pos = parse_expression(pos)
            if pos >= len(expression) or expression[pos] != ')':
                raise ValueError("Mismatched parentheses")
            pos += 1
            return value, pos
        elif pos < len(expression) and expression[pos] == '-':
            pos += 1
            value, pos = parse_factor(pos)
            return -value, pos
        elif pos < len(expression) and expression[pos] == '+':
            pos += 1
            value, pos = parse_factor(pos)
            return value, pos
        else:
            return parse_number(pos)

    def parse_number(pos):
        start = pos
        while pos < len(expression) and (expression[pos].isdigit() or expression[pos] == '.'):
            pos += 1
        if start == pos:
            raise ValueError(f"Unexpected character at position {pos}: {expression[pos] if pos < len(expression) else 'end of string'}")
        num_str = expression[start:pos]
        if '.' in num_str:
            return float(num_str), pos
        else:
            return int(num_str), pos

    pos = 0
    while pos < len(expression) and expression[pos] == ' ':
        pos += 1
    result, pos = parse_expression(pos)
    while pos < len(expression) and expression[pos] == ' ':
        pos += 1
    if pos != len(expression):
        raise ValueError(f"Unexpected character at position {pos}: {expression[pos]}")
    return result

if __name__ == '__main__':
    print(evaluate_expression("3 + 5 * (2 - 8)"))
    print(evaluate_expression("((10 + 2) * 3) / 4"))
    print(evaluate_expression("-5 + 3"))
    print(evaluate_expression("100 / 10"))
    print(evaluate_expression("2 ** 3"))
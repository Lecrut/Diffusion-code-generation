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
            result, pos = parse_expression(pos)
            if pos < len(expression) and expression[pos] == ')':
                pos += 1
            else:
                raise ValueError("Mismatched parentheses")
            return result, pos
        if pos < len(expression) and expression[pos] == '-':
            pos += 1
            val, pos = parse_number(pos)
            return -val, pos
        if pos < len(expression) and expression[pos] == '+':
            pos += 1
            val, pos = parse_number(pos)
            return val, pos
        val, pos = parse_number(pos)
        return val, pos

    def parse_number(pos):
        start = pos
        while pos < len(expression) and (expression[pos].isdigit() or expression[pos] == '.'):
            pos += 1
        if start == pos:
            raise ValueError(f"Unexpected character at position {pos}: {expression[pos] if pos < len(expression) else 'end of string'}")
        num_str = expression[start:pos]
        if '.' in num_str:
            return float(num_str), pos
        return int(num_str), pos

    pos = 0
    result, pos = parse_expression(pos)
    if pos < len(expression):
        raise ValueError(f"Unexpected character at position {pos}: {expression[pos]}")
    return result

if __name__ == '__main__':
    print(evaluate_expression("3 + 5 * (2 - 8)"))
    print(evaluate_expression("10 / 2 + 3"))
    print(evaluate_expression("((1 + 2) * (3 + 4))"))
    print(evaluate_expression("-5 + 10"))
    print(evaluate_expression("100 / (5 * 4)"))
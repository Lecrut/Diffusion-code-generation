def evaluate_expression(expression: str) -> float:
    def parse_expression(tokens, pos):
        left, pos = parse_term(tokens, pos)
        while pos < len(tokens) and tokens[pos] in ('+', '-'):
            op = tokens[pos]
            pos += 1
            right, pos = parse_term(tokens, pos)
            if op == '+':
                left = left + right
            else:
                left = left - right
        return left, pos

    def parse_term(tokens, pos):
        left, pos = parse_factor(tokens, pos)
        while pos < len(tokens) and tokens[pos] in ('*', '/'):
            op = tokens[pos]
            pos += 1
            right, pos = parse_factor(tokens, pos)
            if op == '*':
                left = left * right
            else:
                if right == 0:
                    raise ZeroDivisionError("division by zero")
                left = left / right
        return left, pos

    def parse_factor(tokens, pos):
        if pos < len(tokens) and tokens[pos] == '-':
            pos += 1
            val, pos = parse_factor(tokens, pos)
            return -val, pos
        if pos < len(tokens) and tokens[pos] == '+':
            pos += 1
            val, pos = parse_factor(tokens, pos)
            return val, pos
        return parse_primary(tokens, pos)

    def parse_primary(tokens, pos):
        if pos < len(tokens) and tokens[pos] == '(':
            pos += 1
            val, pos = parse_expression(tokens, pos)
            if pos >= len(tokens) or tokens[pos] != ')':
                raise ValueError("Mismatched parentheses")
            pos += 1
            return val, pos
        if pos < len(tokens) and tokens[pos] == ')':
            raise ValueError("Mismatched parentheses")
        val_str = tokens[pos]
        pos += 1
        if '.' in val_str:
            return float(val_str), pos
        return int(val_str), pos

    tokens = []
    i = 0
    n = len(expression)
    while i < n:
        c = expression[i]
        if c == ' ':
            i += 1
            continue
        if c in '+-*/()':
            tokens.append(c)
            i += 1
        elif c.isdigit() or c == '.':
            j = i
            while j < n and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            tokens.append(expression[i:j])
            i = j
        else:
            raise ValueError(f"Unsupported character: {c}")
    if not tokens:
        raise ValueError("Empty expression")
    result, pos = parse_expression(tokens, 0)
    if pos != len(tokens):
        raise ValueError("Unexpected tokens at end of expression")
    return result

if __name__ == '__main__':
    print(evaluate_expression("3 + 5 * (2 - 8)"))
    print(evaluate_expression("(1 + 2) * (3 + 4)"))
    print(evaluate_expression("10 / 2 + 3"))
    print(evaluate_expression("-5 + 10"))
    print(evaluate_expression("2 ** 3"))
    print(evaluate_expression("100"))
    print(evaluate_expression("((1 + 2))"))
    print(evaluate_expression("3.5 + 2.5"))
    print(evaluate_expression("10 / 3"))
    print(evaluate_expression("2 * 3 + 4 * 5"))
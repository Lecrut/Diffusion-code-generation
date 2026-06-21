def evaluate_expression(expression: str) -> float:
    def _parse_expr(tokens, pos):
        val, pos = _parse_term(tokens, pos)
        while pos < len(tokens) and tokens[pos] in ('+', '-'):
            op = tokens[pos]
            pos += 1
            right, pos = _parse_term(tokens, pos)
            if op == '+':
                val = val + right
            else:
                val = val - right
        return val, pos

    def _parse_term(tokens, pos):
        val, pos = _parse_factor(tokens, pos)
        while pos < len(tokens) and tokens[pos] in ('*', '/'):
            op = tokens[pos]
            pos += 1
            right, pos = _parse_factor(tokens, pos)
            if op == '*':
                val = val * right
            else:
                val = val / right
        return val, pos

    def _parse_factor(tokens, pos):
        if pos < len(tokens) and tokens[pos] == '(':
            pos += 1
            val, pos = _parse_expr(tokens, pos)
            if pos < len(tokens) and tokens[pos] == ')':
                pos += 1
            return val, pos
        if pos < len(tokens) and tokens[pos] == '-':
            pos += 1
            val, pos = _parse_factor(tokens, pos)
            return -val, pos
        if pos < len(tokens) and tokens[pos] == '+':
            pos += 1
            val, pos = _parse_factor(tokens, pos)
            return val, pos
        if pos < len(tokens):
            val = float(tokens[pos])
            pos += 1
            return val, pos
        raise ValueError("Unexpected end of expression")

    tokens = []
    i = 0
    n = len(expression)
    while i < n:
        char = expression[i]
        if char.isspace():
            i += 1
            continue
        if char in '+-*/()':
            tokens.append(char)
            i += 1
        elif char.isdigit() or char == '.':
            j = i
            while j < n and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            tokens.append(expression[i:j])
            i = j
        else:
            raise ValueError(f"Invalid character: {char}")
    
    if not tokens:
        return 0.0
    
    result, end_pos = _parse_expr(tokens, 0)
    return result

if __name__ == '__main__':
    print(evaluate_expression("3 + 4 * 2 / (1 - 5)"))
    print(evaluate_expression("10 - 2 * 3"))
    print(evaluate_expression("(2 + 3) * (4 - 1)"))
    print(evaluate_expression("-5 + 10"))
    print(evaluate_expression("100 / 10 / 2"))
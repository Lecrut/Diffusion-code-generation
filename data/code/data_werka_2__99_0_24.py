def evaluate_expression(expression: str) -> float:
    def parse_expression(tokens, pos):
        result, pos = parse_term(tokens, pos)
        while pos < len(tokens) and tokens[pos] in ('+', '-'):
            op = tokens[pos]
            pos += 1
            right, pos = parse_term(tokens, pos)
            if op == '+':
                result += right
            else:
                result -= right
        return result, pos

    def parse_term(tokens, pos):
        result, pos = parse_factor(tokens, pos)
        while pos < len(tokens) and tokens[pos] in ('*', '/'):
            op = tokens[pos]
            pos += 1
            right, pos = parse_factor(tokens, pos)
            if op == '*':
                result *= right
            else:
                if right == 0:
                    raise ZeroDivisionError("division by zero")
                result /= right
        return result, pos

    def parse_factor(tokens, pos):
        if pos < len(tokens) and tokens[pos] == '-':
            pos += 1
            val, pos = parse_factor(tokens, pos)
            return -val, pos
        if pos < len(tokens) and tokens[pos] == '+':
            pos += 1
            val, pos = parse_factor(tokens, pos)
            return val, pos
        if pos < len(tokens) and tokens[pos] == '(':
            pos += 1
            val, pos = parse_expression(tokens, pos)
            if pos >= len(tokens) or tokens[pos] != ')':
                raise ValueError("Mismatched parentheses")
            pos += 1
            return val, pos
        if pos < len(tokens):
            token = tokens[pos]
            try:
                if '.' in token or 'e' in token.lower():
                    val = float(token)
                else:
                    val = int(token)
                pos += 1
                return val, pos
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
        raise ValueError("Unexpected end of expression")

    def tokenize(expr):
        tokens = []
        i = 0
        while i < len(expr):
            char = expr[i]
            if char.isspace():
                i += 1
                continue
            if char in '()+*/-':
                tokens.append(char)
                i += 1
                continue
            if char.isdigit() or char == '.':
                start = i
                while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                    i += 1
                tokens.append(expr[start:i])
                continue
            if char == 'e' or char == 'E':
                start = i
                i += 1
                if i < len(expr) and (expr[i].isdigit() or expr[i] == '+' or expr[i] == '-'):
                    while i < len(expr) and (expr[i].isdigit() or expr[i] in '+-'):
                        i += 1
                    tokens.append(expr[start:i])
                    continue
                else:
                    raise ValueError(f"Invalid character at position {i}: {char}")
            raise ValueError(f"Invalid character at position {i}: {char}")
        return tokens

    tokens = tokenize(expression)
    if not tokens:
        raise ValueError("Empty expression")
    result, pos = parse_expression(tokens, 0)
    if pos != len(tokens):
        raise ValueError("Unexpected tokens at end of expression")
    return result

if __name__ == '__main__':
    print(evaluate_expression("3 + 5 * 2"))
    print(evaluate_expression("(10 - 2) / 4"))
    print(evaluate_expression("2 ** 3 + 1"))
    print(evaluate_expression("100 / 10"))
    print(evaluate_expression("-5 + 3"))
    print(evaluate_expression("((2 + 3) * (4 - 1))"))
    print(evaluate_expression("1.5 + 2.5 * 3"))
    print(evaluate_expression("10 - (3 + 2)"))
    print(evaluate_expression("2 * 3 + 4 * 5"))
    print(evaluate_expression("10 / (2 + 3)"))
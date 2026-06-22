def evaluate_expression(expression: str) -> float:
    tokens = []
    i = 0
    length = len(expression)
    while i < length:
        char = expression[i]
        if char.isspace():
            i += 1
            continue
        if char in '0123456789.':
            num_str = ''
            while i < length and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                i += 1
            if '.' in num_str:
                tokens.append(float(num_str))
            else:
                tokens.append(int(num_str))
            continue
        if char in '+-*/()':
            tokens.append(char)
            i += 1
            continue
        raise ValueError(f"Unsupported character: {char}")

    pos = 0

    def parse_expression():
        nonlocal pos
        left, pos = parse_term()
        while pos < len(tokens) and tokens[pos] in ('+', '-'):
            op = tokens[pos]
            pos += 1
            right, pos = parse_term()
            if op == '+':
                left = left + right
            else:
                left = left - right
        return left, pos

    def parse_term():
        nonlocal pos
        left, pos = parse_factor()
        while pos < len(tokens) and tokens[pos] in ('*', '/'):
            op = tokens[pos]
            pos += 1
            right, pos = parse_factor()
            if op == '*':
                left = left * right
            else:
                left = left / right
        return left, pos

    def parse_factor():
        nonlocal pos
        if pos < len(tokens) and tokens[pos] == '-':
            pos += 1
            val, pos = parse_factor()
            return -val, pos
        if pos < len(tokens) and tokens[pos] == '+':
            pos += 1
            val, pos = parse_factor()
            return val, pos
        return parse_power()

    def parse_power():
        nonlocal pos
        base, pos = parse_primary()
        if pos < len(tokens) and tokens[pos] == '**':
            pos += 1
            exp, pos = parse_primary()
            return base ** exp, pos
        return base, pos

    def parse_primary():
        nonlocal pos
        if pos >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token = tokens[pos]
        if token == '(':
            pos += 1
            val, pos = parse_expression()
            if pos < len(tokens) and tokens[pos] == ')':
                pos += 1
            else:
                raise ValueError("Missing closing parenthesis")
            return val, pos
        if isinstance(token, (int, float)):
            pos += 1
            return token, pos
        raise ValueError(f"Unexpected token: {token}")

    result, _ = parse_expression()
    return result

if __name__ == '__main__':
    print(evaluate_expression("3 + 4 * 2"))
    print(evaluate_expression("(3 + 4) * 2"))
    print(evaluate_expression("10 - 2 * 3"))
    print(evaluate_expression("2 ** 3"))
    print(evaluate_expression("10 / 3"))
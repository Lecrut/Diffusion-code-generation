def parse_expression(expr):
    def parse_term():
        result = parse_factor()
        while True:
            if pos < len(expr) and expr[pos] == '*':
                pos_advance()
                right = parse_factor()
                result = result * right
            elif pos < len(expr) and expr[pos] == '/':
                pos_advance()
                right = parse_factor()
                result = result / right
            else:
                break
        return result

    def parse_factor():
        if pos < len(expr) and expr[pos] == '(':
            pos_advance()
            result = parse_expression()
            if pos < len(expr) and expr[pos] == ')':
                pos_advance()
            else:
                raise ValueError("Missing closing parenthesis")
            return result
        elif pos < len(expr) and expr[pos] == '-':
            pos_advance()
            return -parse_factor()
        elif pos < len(expr) and expr[pos] == '+':
            pos_advance()
            return parse_factor()
        else:
            start = pos
            while pos < len(expr) and (expr[pos].isdigit() or expr[pos] == '.'):
                pos += 1
            if start == pos:
                raise ValueError(f"Unexpected character at position {pos}: {expr[pos] if pos < len(expr) else 'end of string'}")
            return float(expr[start:pos])

    def parse_addition():
        result = parse_term()
        while True:
            if pos < len(expr) and expr[pos] == '+':
                pos_advance()
                right = parse_term()
                result = result + right
            elif pos < len(expr) and expr[pos] == '-':
                pos_advance()
                right = parse_term()
                result = result - right
            else:
                break
        return result

    def pos_advance():
        nonlocal pos
        while pos < len(expr) and expr[pos] == ' ':
            pos += 1

    pos = 0
    while pos < len(expr) and expr[pos] == ' ':
        pos += 1
    result = parse_addition()
    while pos < len(expr) and expr[pos] == ' ':
        pos += 1
    if pos != len(expr):
        raise ValueError(f"Unexpected character at position {pos}: {expr[pos]}")
    return result

if __name__ == '__main__':
    print(parse_expression("( 1 + 2 ) * ( 3 + 4 )"))
    print(parse_expression("((10 - 5) / (2 + 3))"))
    print(parse_expression("((2 + 3) * (4 - 1))"))
    print(parse_expression("((1 + 2) * (3 + 4))"))
    print(parse_expression("((10 / 2) + (3 * 4))"))
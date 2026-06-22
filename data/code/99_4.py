def parse_expression(expr):
    def parse_term():
        nonlocal pos
        if pos < len(expr) and expr[pos] == '(':
            pos += 1
            result = parse_expr()
            if pos < len(expr) and expr[pos] == ')':
                pos += 1
                return result
            else:
                raise ValueError("Missing closing parenthesis")
        else:
            num_str = ""
            while pos < len(expr) and (expr[pos].isdigit() or expr[pos] == '.'):
                num_str += expr[pos]
                pos += 1
            if not num_str:
                raise ValueError("Expected number or parenthesis")
            return float(num_str) if '.' in num_str else int(num_str)

    def parse_expr():
        nonlocal pos
        left = parse_term()
        while pos < len(expr) and expr[pos] in '+-':
            op = expr[pos]
            pos += 1
            right = parse_term()
            if op == '+':
                left = left + right
            else:
                left = left - right
        return left

    pos = 0
    while pos < len(expr) and expr[pos] == ' ':
        pos += 1
    result = parse_expr()
    while pos < len(expr) and expr[pos] == ' ':
        pos += 1
    if pos != len(expr):
        raise ValueError("Unexpected characters after expression")
    return result

if __name__ == '__main__':
    print(parse_expression("(1 + 2) * (3 + 4)"))
    print(parse_expression("((10 - 5) / (2 + 3))"))
    print(parse_expression("((1 + 2) * ((3 + 4) - 1))"))
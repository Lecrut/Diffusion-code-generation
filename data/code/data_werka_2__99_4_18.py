def evaluate_expression(expr: str) -> float:
    expr = expr.replace(" ", "")
    pos = [0]

    def parse_expr():
        val = parse_term()
        while pos[0] < len(expr) and expr[pos[0]] in ('+', '-'):
            op = expr[pos[0]]
            pos[0] += 1
            right = parse_term()
            if op == '+':
                val += right
            else:
                val -= right
        return val

    def parse_term():
        val = parse_factor()
        while pos[0] < len(expr) and expr[pos[0]] in ('*', '/'):
            op = expr[pos[0]]
            pos[0] += 1
            right = parse_factor()
            if op == '*':
                val *= right
            else:
                if right == 0:
                    raise ValueError("Division by zero")
                val /= right
        return val

    def parse_factor():
        if pos[0] >= len(expr):
            raise ValueError("Unexpected end of expression")
        if expr[pos[0]] == '(':
            pos[0] += 1
            val = parse_expr()
            if pos[0] >= len(expr) or expr[pos[0]] != ')':
                raise ValueError("Missing closing parenthesis")
            pos[0] += 1
            return val
        else:
            return parse_number()

    def parse_number():
        start = pos[0]
        if pos[0] < len(expr) and expr[pos[0]] == '-':
            pos[0] += 1
        while pos[0] < len(expr) and (expr[pos[0]].isdigit() or expr[pos[0]] == '.'):
            pos[0] += 1
        if pos[0] == start or (start == pos[0] - 1 and expr[start] == '-'):
            raise ValueError("Invalid number")
        return float(expr[start:pos[0]])

    result = parse_expr()
    if pos[0] != len(expr):
        raise ValueError("Unexpected characters at end of expression")
    return result

if __name__ == '__main__':
    print(evaluate_expression("((1+2)*(3+4))"))
    print(evaluate_expression("((10/2)+5)"))
    print(evaluate_expression("(((2+3)*(4-1))/5)"))
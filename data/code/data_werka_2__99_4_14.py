def parse_expression(expr):
    def parse_term():
        nonlocal pos
        if pos < len(expr) and expr[pos] == '(':
            pos += 1
            result = parse_expression()
            if pos < len(expr) and expr[pos] == ')':
                pos += 1
            return result
        else:
            num_str = ''
            while pos < len(expr) and (expr[pos].isdigit() or expr[pos] == '.'):
                num_str += expr[pos]
                pos += 1
            if not num_str:
                raise ValueError("Expected number or parenthesis")
            return float(num_str) if '.' in num_str else int(num_str)

    def parse_factor():
        nonlocal pos
        if pos < len(expr) and expr[pos] == '-':
            pos += 1
            return -parse_term()
        return parse_term()

    def parse_expression():
        nonlocal pos
        result = parse_factor()
        while pos < len(expr) and expr[pos] in ('+', '-'):
            op = expr[pos]
            pos += 1
            right = parse_factor()
            if op == '+':
                result += right
            else:
                result -= right
        return result

    pos = 0
    while pos < len(expr) and expr[pos] == ' ':
        pos += 1
    result = parse_expression()
    return result

if __name__ == '__main__':
    expression = "( 3 + ( 4 * 5 ) ) - ( 2 + 1 )"
    result = parse_expression(expression)
    print(result)
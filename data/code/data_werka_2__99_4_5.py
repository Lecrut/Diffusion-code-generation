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
            num_str = ''
            while pos < len(expr) and (expr[pos].isdigit() or expr[pos] == '.'):
                num_str += expr[pos]
                pos += 1
            if not num_str:
                raise ValueError("Expected number or parenthesis")
            return float(num_str) if '.' in num_str else int(num_str)

    def parse_expr():
        nonlocal pos
        result = parse_term()
        while pos < len(expr) and expr[pos] in '+-':
            op = expr[pos]
            pos += 1
            right = parse_term()
            if op == '+':
                result += right
            else:
                result -= right
        return result

    pos = 0
    expr = expr.replace(' ', '')
    if not expr:
        raise ValueError("Empty expression")
    result = parse_expr()
    if pos != len(expr):
        raise ValueError("Unexpected characters at end of expression")
    return result

if __name__ == '__main__':
    expression = "(3 + (4 * 5))"
    result = parse_expression(expression)
    print(result)
    
    expression2 = "((10 - 2) / (3 + 1))"
    result2 = parse_expression(expression2)
    print(result2)
    
    expression3 = "((2 + 3) * (4 - 1))"
    result3 = parse_expression(expression3)
    print(result3)
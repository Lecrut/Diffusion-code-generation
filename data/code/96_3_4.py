def evaluate_nested_expression(expr):
    if isinstance(expr, bool):
        return expr
    if len(expr) == 3:
        left = evaluate_nested_expression(expr[0])
        op = expr[1]
        right = evaluate_nested_expression(expr[2])
        if op == 'AND':
            return left and right
        elif op == 'OR':
            return left or right
        elif op == 'XOR':
            return left ^ right
        elif op == 'NAND':
            return not (left and right)
        elif op == 'NOR':
            return not (left or right)
        else:
            raise ValueError(f"Unsupported operator: {op}")
    if len(expr) == 2:
        operand = evaluate_nested_expression(expr[0])
        op = expr[1]
        if op == 'NOT':
            return not operand
        else:
            raise ValueError(f"Unsupported unary operator: {op}")
    raise ValueError(f"Invalid expression structure: {expr}")

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    expr = ['AND', ['AND', ['AND', A, B], C], D]
    result = evaluate_nested_expression(expr)
    print(result)
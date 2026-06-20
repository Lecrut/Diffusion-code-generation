operators = {
    'and': lambda x, y: x and y,
    'or': lambda x, y: x or y,
    'not': lambda x: not x,
}

def evaluate_expression(X, Y, Z, W):
    expr_parts = [
        (X, 'and', Y),
        ('not', Z),
        (W, 'and', 'True')
    ]
    result = False
    for part in expr_parts:
        if isinstance(part[1], tuple):
            left, op, right = part
            result = operators[op](left, right)
        else:
            operator, operand = part
            result = operators[operator](operand)
    return result

if __name__ == '__main__':
    result = evaluate_expression(True, False, True, False)
    print(result)
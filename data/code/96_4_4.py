def evaluate_expression(X, Y, Z, W):
    operators = {
        'and': lambda x, y: x and y,
        'or': lambda x, y: x or y,
        'not': lambda x: not x,
        'xor': lambda x, y: x != y
    }
    expr_parts = [(X, 'and', Y), (Z, 'and', 'not'), W]
    result = False
    for part in expr_parts:
        if isinstance(part, tuple):
            left, op, right = part
            result = operators[op](left, right)
        else:
            result = operators['or'](result, part)
    return result

if __name__ == '__main__':
    result = evaluate_expression(True, False, True, False)
    print(result)
def evaluate_expression(X, Y, Z, W):
    operations = {'and': lambda x, y: x and y, 'or': lambda x, y: x or y, 'not': lambda x: not x}
    expr_parts = [(X, 'and', Y), (Z, 'and', not W)]
    result = False
    for part in expr_parts:
        if isinstance(part, tuple):
            left, op, right = part
            result = operations[op](left, right)
        else:
            result = operations['or'](result, part)
    return result
if __name__ == '__main__':
    result = evaluate_expression(True, False, True, False)
    print(result)
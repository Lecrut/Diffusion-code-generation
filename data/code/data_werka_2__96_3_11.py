def evaluate_nested_expression(expr):
    if not isinstance(expr, list):
        if isinstance(expr, bool):
            return expr
        raise ValueError("Unsupported input type")
    
    if len(expr) == 0:
        raise ValueError("Empty expression")
    
    if len(expr) == 1:
        return evaluate_nested_expression(expr[0])
    
    if len(expr) == 2:
        left = evaluate_nested_expression(expr[0])
        right = evaluate_nested_expression(expr[1])
        if isinstance(expr[0], list) and isinstance(expr[1], list):
            return (left, right)
        return (left, right)
    
    if len(expr) == 3:
        op = expr[1]
        left = evaluate_nested_expression(expr[0])
        right = evaluate_nested_expression(expr[2])
        
        if op == 'and':
            return left and right
        elif op == 'or':
            return left or right
        elif op == 'nand':
            return not (left and right)
        elif op == 'nor':
            return not (left or right)
        elif op == 'xor':
            return left ^ right
        elif op == 'implies':
            return (not left) or right
        else:
            raise ValueError(f"Unsupported operator: {op}")
    
    raise ValueError("Unsupported expression length")

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    
    expr = [
        [
            [
                [A, 'and', B],
                'or',
                C
            ],
            'and',
            D
        ]
    ]
    
    result = evaluate_nested_expression(expr)
    print(result)
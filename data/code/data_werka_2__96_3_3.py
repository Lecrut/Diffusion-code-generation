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
        if isinstance(left, bool) and isinstance(right, bool):
            return left and right
        raise ValueError("Unsupported operands")
    
    if len(expr) == 3:
        op = expr[1]
        left = evaluate_nested_expression(expr[0])
        right = evaluate_nested_expression(expr[2])
        
        if op == 'and':
            if isinstance(left, bool) and isinstance(right, bool):
                return left and right
        elif op == 'or':
            if isinstance(left, bool) and isinstance(right, bool):
                return left or right
        elif op == 'xor':
            if isinstance(left, bool) and isinstance(right, bool):
                return left ^ right
        elif op == 'nand':
            if isinstance(left, bool) and isinstance(right, bool):
                return not (left and right)
        elif op == 'nor':
            if isinstance(left, bool) and isinstance(right, bool):
                return not (left or right)
        elif op == 'implies':
            if isinstance(left, bool) and isinstance(right, bool):
                return (not left) or right
        else:
            raise ValueError(f"Unsupported operator: {op}")
        
        raise ValueError("Unsupported operands")
    
    if len(expr) == 4:
        op = expr[1]
        left = evaluate_nested_expression(expr[0])
        right = evaluate_nested_expression(expr[2])
        result = evaluate_nested_expression(expr[3])
        
        if op == 'and':
            if isinstance(left, bool) and isinstance(right, bool) and isinstance(result, bool):
                return left and right and result
        elif op == 'or':
            if isinstance(left, bool) and isinstance(right, bool) and isinstance(result, bool):
                return left or right or result
        else:
            raise ValueError(f"Unsupported operator for 4-element list: {op}")
        
        raise ValueError("Unsupported operands")
    
    raise ValueError("Unsupported expression length")

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    
    expr = [[['A', 'and', 'B'], 'or', 'C'], 'and', 'D']
    
    def resolve(expr):
        if isinstance(expr, str):
            if expr == 'A':
                return A
            elif expr == 'B':
                return B
            elif expr == 'C':
                return C
            elif expr == 'D':
                return D
            else:
                raise ValueError(f"Unknown variable: {expr}")
        return evaluate_nested_expression(expr)
    
    result = resolve(expr)
    print(result)
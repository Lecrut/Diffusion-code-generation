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
        raise ValueError("Unsupported operands for AND")
    
    if len(expr) == 3:
        op = expr[0]
        left = evaluate_nested_expression(expr[1])
        right = evaluate_nested_expression(expr[2])
        
        if op == 'and':
            if isinstance(left, bool) and isinstance(right, bool):
                return left and right
            raise ValueError("Unsupported operands for AND")
        elif op == 'or':
            if isinstance(left, bool) and isinstance(right, bool):
                return left or right
            raise ValueError("Unsupported operands for OR")
        elif op == 'xor':
            if isinstance(left, bool) and isinstance(right, bool):
                return left ^ right
            raise ValueError("Unsupported operands for XOR")
        elif op == 'nand':
            if isinstance(left, bool) and isinstance(right, bool):
                return not (left and right)
            raise ValueError("Unsupported operands for NAND")
        elif op == 'nor':
            if isinstance(left, bool) and isinstance(right, bool):
                return not (left or right)
            raise ValueError("Unsupported operands for NOR")
        else:
            raise ValueError(f"Unsupported operator: {op}")
    
    if len(expr) == 4:
        op = expr[0]
        left = evaluate_nested_expression(expr[1])
        right = evaluate_nested_expression(expr[2])
        third = evaluate_nested_expression(expr[3])
        
        if op == 'and':
            if isinstance(left, bool) and isinstance(right, bool) and isinstance(third, bool):
                return left and right and third
            raise ValueError("Unsupported operands for AND")
        elif op == 'or':
            if isinstance(left, bool) and isinstance(right, bool) and isinstance(third, bool):
                return left or right or third
            raise ValueError("Unsupported operands for OR")
        else:
            raise ValueError(f"Unsupported operator for 4-element list: {op}")
    
    raise ValueError("Unsupported expression structure")

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    
    expr = ['and', ['and', ['and', A, B], C], D]
    result = evaluate_nested_expression(expr)
    print(result)
    
    expr2 = ['or', ['or', ['or', A, B], C], D]
    result2 = evaluate_nested_expression(expr2)
    print(result2)
    
    expr3 = ['xor', ['xor', ['xor', A, B], C], D]
    result3 = evaluate_nested_expression(expr3)
    print(result3)
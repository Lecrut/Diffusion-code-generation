def evaluate_expression(expression):
    TRUE_VAL = True
    FALSE_VAL = False
    
    if isinstance(expression, bool):
        return expression
    
    if not isinstance(expression, list):
        raise ValueError(f"Unsupported type: {type(expression)}")
    
    if len(expression) == 0:
        raise ValueError("Empty expression")
    
    if len(expression) == 1:
        return evaluate_expression(expression[0])
    
    if len(expression) == 2:
        left = evaluate_expression(expression[0])
        right = evaluate_expression(expression[1])
        if isinstance(left, bool) and isinstance(right, bool):
            return left and right
        raise ValueError("Operands must be boolean")
    
    if len(expression) == 3:
        op = expression[1]
        left = evaluate_expression(expression[0])
        right = evaluate_expression(expression[2])
        
        if op == 'AND':
            return left and right
        if op == 'OR':
            return left or right
        if op == 'XOR':
            return left ^ right
        if op == 'NAND':
            return not (left and right)
        if op == 'NOR':
            return not (left or right)
        if op == 'NOT':
            return not left
        raise ValueError(f"Unknown operator: {op}")
    
    raise ValueError("Unsupported expression structure")

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    
    expr = ['AND', ['AND', ['AND', A, B], C], D]
    result = evaluate_expression(expr)
    print(result)
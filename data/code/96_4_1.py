def evaluate_expression(expression):
    if len(expression) == 1:
        return expression[0]
    else:
        left = evaluate_expression(expression[0])
        right = evaluate_expression(expression[1])
        operator = expression[2]
        result = None
        if operator == 'and':
            result = left and right
        elif operator == 'or':
            result = left or right
        elif operator == 'not':
            result = not left
        elif operator == 'xor':
            result = left ^ right
        else:
            raise ValueError("Unknown operator")
        return result
if __name__ == '__main__':
    sample_expression = [
        'and',
        [True, False],
        'or',
        [True, True],
        'and',
        [True, False]
    ]
    def evaluate_nested(expr):
        if len(expr) == 1:
            return expr[0]
        left_expr = evaluate_nested(expr[0])
        operator = expr[1]
        right_expr = evaluate_nested(expr[2])
        if operator == 'and':
            return left_expr and right_expr
        elif operator == 'or':
            return left_expr or right_expr
        elif operator == 'not':
            return not left_expr
        elif operator == 'xor':
            return left_expr ^ right_expr
        else:
            raise ValueError("Unknown operator")
    test_expression = [
        [True, 'and', False],            
        [True, 'or', True],                     
        [True, 'and', False]                           
    ]
    try:
        result = evaluate_nested(test_expression)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
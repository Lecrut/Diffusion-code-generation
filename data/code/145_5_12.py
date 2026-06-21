def de_morgan_optimize(expression):
    if isinstance(expression, tuple) and len(expression) == 3:
        operator = expression[0]
        left = expression[1]
        right = expression[2]
        
        if operator == 'and':
            return ('or', ('not', left), ('not', right))
        elif operator == 'or':
            return ('and', ('not', left), ('not', right))
    
    return expression

def flatten_expression(expression):
    stack = [expression]
    result = []
    
    while stack:
        current = stack.pop()
        
        if isinstance(current, tuple) and len(current) == 3:
            operator, left, right = current
            
            if operator in ('and', 'or'):
                stack.append(de_morgan_optimize(('not', ('not', operator), left, right)))
            else:
                result.append(current)
        else:
            result.append(current)
    
    return result

if __name__ == '__main__':
    sample_expression = (('and', True, False), ('or', True, False))
    flattened_expression = flatten_expression(sample_expression)
    print(flattened_expression)
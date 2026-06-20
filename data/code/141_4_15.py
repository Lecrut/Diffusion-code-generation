def combine_booleans(ops, *bools):
    operators = {'AND': lambda x, y: x and y,
                 'OR': lambda x, y: x or y,
                 'NOT': lambda x: not x}
    
    if len(bools) < 2:
        raise ValueError("At least two boolean values are required")
    
    result = bools[0]
    for op, b in zip(ops, bools[1:]):
        if op not in operators:
            raise ValueError(f"Invalid operator: {op}")
        
        result = operators[op](result, b)
    
    return result

if __name__ == '__main__':
    A = True
    B = False
    C = True
    print(combine_booleans(['NOT', 'AND'], A, B, C))
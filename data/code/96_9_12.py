def evaluate_nested_logic(nested):
    if isinstance(nested, list):
        return all(evaluate_nested_logic(item) for item in nested)
    elif isinstance(nested, tuple):
        operator = nested[0]
        operands = nested[1:]
        if operator == 'and':
            return all(evaluate_nested_logic(operand) for operand in operands)
        elif operator == 'or':
            return any(evaluate_nested_logic(operand) for operand in operands)
    else:
        return nested

if __name__ == '__main__':
    sample = ('and', ('or', True, False), True)
    print(evaluate_nested_logic(sample))
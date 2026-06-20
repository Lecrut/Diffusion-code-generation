def evaluate_nested_logic(nested):
    if isinstance(nested, list):
        return all(evaluate_nested_logic(x) for x in nested)
    elif isinstance(nested, tuple):
        operator = nested[0]
        operands = nested[1:]
        if operator == 'and':
            return all(evaluate_nested_logic(x) for x in operands)
        elif operator == 'or':
            return any(evaluate_nested_logic(x) for x in operands)
        else:
            raise ValueError(f"Unknown operator: {operator}")
    else:
        return nested

if __name__ == '__main__':
    print(evaluate_nested_logic(('and', True, ('or', False, True))))
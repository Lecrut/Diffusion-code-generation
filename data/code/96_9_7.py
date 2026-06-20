def evaluate_nested_logic(nested):
    if isinstance(nested, list) or isinstance(nested, tuple):
        operator = nested[0]
        operands = nested[1:]
        if operator == 'and':
            return all(evaluate_nested_logic(op) for op in operands)
        elif operator == 'or':
            return any(evaluate_nested_logic(op) for op in operands)
    else:
        return nested

if __name__ == '__main__':
    sample_input = ['and', [True, False], ['or', True, False]]
    result = evaluate_nested_logic(sample_input)
    print(result)
def evaluate_nested_logic(nested):
    if isinstance(nested, list) or isinstance(nested, tuple):
        operator = nested[0]
        args = nested[1:]
        if operator == 'and':
            return all(evaluate_nested_logic(arg) for arg in args)
        elif operator == 'or':
            return any(evaluate_nested_logic(arg) for arg in args)
    return nested

if __name__ == '__main__':
    sample_input = ['and', [True, False], ['or', True, False]]
    print(evaluate_nested_logic(sample_input))
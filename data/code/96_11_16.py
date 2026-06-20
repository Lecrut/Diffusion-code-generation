def evaluate_nested_logic(logic_structure):
    if isinstance(logic_structure, bool):
        return logic_structure
    elif not isinstance(logic_structure, list) and (not isinstance(logic_structure, tuple)):
        raise ValueError('Invalid input: Expected a boolean or a list/tuple of booleans')
    results = []
    for item in logic_structure:
        result = evaluate_nested_logic(item)
        if result:
            return True
        results.append(result)
    return any(results)
if __name__ == '__main__':
    sample1 = [True, False]
    sample2 = [False, [True, False]]
    sample3 = [[False], [False], [True]]
    print(evaluate_nested_logic(sample1))
    print(evaluate_nested_logic(sample2))
    print(evaluate_nested_logic(sample3))
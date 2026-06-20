def evaluate_nested_logic(logic_structure):
    if isinstance(logic_structure, bool):
        return logic_structure
    elif isinstance(logic_structure, list) or isinstance(logic_structure, tuple):
        results = [evaluate_nested_logic(item) for item in logic_structure]
        if any(results):
            return True
        else:
            return False
    else:
        return False
if __name__ == '__main__':
    sample1 = [False, [True, False]]
    sample2 = [[False], True]
    sample3 = [[[False], False], True]
    print(evaluate_nested_logic(sample1))
    print(evaluate_nested_logic(sample2))
    print(evaluate_nested_logic(sample3))
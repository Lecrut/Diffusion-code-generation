def evaluate_nested_logic(logic_structure):
    if isinstance(logic_structure, bool):
        return logic_structure
    elif isinstance(logic_structure, list) or isinstance(logic_structure, tuple):
        for item in logic_structure:
            result = evaluate_nested_logic(item)
            if result:
                return True
        return False
    else:
        raise ValueError('Invalid input type')
if __name__ == '__main__':
    sample1 = [True, False]
    sample2 = [True, True, False]
    sample3 = [True]
    sample4 = [False]
    print(evaluate_nested_logic(sample1))
    print(evaluate_nested_logic(sample2))
    print(evaluate_nested_logic(sample3))
    print(evaluate_nested_logic(sample4))
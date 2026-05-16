def evaluate_nested_booleans(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            if evaluate_nested_booleans(item):
                return True
        elif isinstance(item, bool):
            if item:
                return True
    return False
if __name__ == '__main__':
    structure1 = [[True], [False, [False, True]], [False]]
    print(evaluate_nested_booleans(structure1))
    structure2 = [[False, [False, False]], [True]]
    print(evaluate_nested_booleans(structure2))
    structure3 = [[False, [False, [False, [False, False]]]]]
    print(evaluate_nested_booleans(structure3))
    structure4 = [[False, False], [False, False]]
    print(evaluate_nested_booleans(structure4))
    structure5 = [[False, False, [False, True]], [False]]
    print(evaluate_nested_booleans(structure5))
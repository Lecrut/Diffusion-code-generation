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
    structure1 = [[True, False], [False, False]]
    structure2 = [[False, False], [True, False]]
    structure3 = [[False, False], [False, False]]
    structure4 = [[True], [False, [False, True]]]
    structure5 = [[False, [True, [False, False]]], [False]]
    print(f"Structure 1 evaluates to True: {evaluate_nested_booleans(structure1)}")
    print(f"Structure 2 evaluates to True: {evaluate_nested_booleans(structure2)}")
    print(f"Structure 3 evaluates to True: {evaluate_nested_booleans(structure3)}")
    print(f"Structure 4 evaluates to True: {evaluate_nested_booleans(structure4)}")
    print(f"Structure 5 evaluates to True: {evaluate_nested_booleans(structure5)}")
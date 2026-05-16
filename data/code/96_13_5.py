def evaluate_nested_boolean(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            if evaluate_nested_boolean(item):
                return True
        elif isinstance(item, bool):
            if item:
                return True
    return False
if __name__ == '__main__':
    structure1 = [[True], [False, [True, False]], [False]]
    structure2 = [[False, [False, [False, [True]]]], [True]]
    structure3 = [[False, [False, [False]]], [False]]
    structure4 = [[False, [False, [False, [False]]]]]
    structure5 = [[False, [False, [False, [False, [False]]]]]]
    print(f"Structure 1 result: {evaluate_nested_boolean(structure1)}")
    print(f"Structure 2 result: {evaluate_nested_boolean(structure2)}")
    print(f"Structure 3 result: {evaluate_nested_boolean(structure3)}")
    print(f"Structure 4 result: {evaluate_nested_boolean(structure4)}")
    print(f"Structure 5 result: {evaluate_nested_boolean(structure5)}")
def evaluate_nested_booleans(nested_bools):
    stack = []
    for item in reversed(nested_bools):
        if isinstance(item, bool):
            stack.append(item)
        else:
            if isinstance(item, list) or isinstance(item, tuple):
                stack.extend(evaluate_nested_booleans(item))
            else:
                raise TypeError("Unsupported data type encountered")
    return stack
if __name__ == '__main__':
    test_structure_1 = [True, [False, True], [True, [False, False]], True]
    test_structure_2 = [True, [False, [True, [False, True]]], True]
    test_structure_3 = [False, [True, [False, [True, [False, False]]]]]
    result_1 = evaluate_nested_booleans(test_structure_1)
    print(f"Result 1: {result_1}")
    result_2 = evaluate_nested_booleans(test_structure_2)
    print(f"Result 2: {result_2}")
    result_3 = evaluate_nested_booleans(test_structure_3)
    print(f"Result 3: {result_3}")
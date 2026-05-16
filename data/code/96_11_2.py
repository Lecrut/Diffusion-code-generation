def evaluate_nested_logic(logic_structure):
    if isinstance(logic_structure, bool):
        return logic_structure
    elif isinstance(logic_structure, list) or isinstance(logic_structure, tuple):
        if not logic_structure:
            return False
        if len(logic_structure) == 1:
            return evaluate_nested_logic(logic_structure[0])
        else:
            results = [evaluate_nested_logic(item) for item in logic_structure]
            return all(results)
    else:
        return False
if __name__ == '__main__':
    sample1 = [True, False]
    sample2 = [True, True, False]
    sample3 = [True]
    sample4 = [False]
    sample5 = [True, True]
    sample6 = [False, False]
    sample7 = [True, False, [True, False], [True]]
    sample8 = [True, [False, [True, False]], True]
    sample9 = []
    sample10 = [True, True, True]
    print(f"Sample 1: {evaluate_nested_logic(sample1)}")
    print(f"Sample 2: {evaluate_nested_logic(sample2)}")
    print(f"Sample 3: {evaluate_nested_logic(sample3)}")
    print(f"Sample 4: {evaluate_nested_logic(sample4)}")
    print(f"Sample 5: {evaluate_nested_logic(sample5)}")
    print(f"Sample 6: {evaluate_nested_logic(sample6)}")
    print(f"Sample 7: {evaluate_nested_logic(sample7)}")
    print(f"Sample 8: {evaluate_nested_logic(sample8)}")
    print(f"Sample 9: {evaluate_nested_logic(sample9)}")
    print(f"Sample 10: {evaluate_nested_logic(sample10)}")
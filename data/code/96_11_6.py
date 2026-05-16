def evaluate_nested_logic(logic_structure):
    if isinstance(logic_structure, bool):
        return logic_structure
    elif isinstance(logic_structure, list) or isinstance(logic_structure, tuple):
        if not logic_structure:
            return False
        if len(logic_structure) == 1:
            return evaluate_nested_logic(logic_structure[0])
        if len(logic_structure) > 1:
            results = [evaluate_nested_logic(item) for item in logic_structure]
            if all(results):
                return True
            if any(results):
                return True
            return False
        return False
    return False
if __name__ == '__main__':
    sample1 = [True, True]
    sample2 = [False, True]
    sample3 = [True, False, True]
    sample4 = [False]
    sample5 = [True, True, True]
    sample6 = []
    sample7 = [False, False]
    sample8 = [True]
    sample9 = [False, True, False]
    print(f"Sample 1: {evaluate_nested_logic(sample1)}")
    print(f"Sample 2: {evaluate_nested_logic(sample2)}")
    print(f"Sample 3: {evaluate_nested_logic(sample3)}")
    print(f"Sample 4: {evaluate_nested_logic(sample4)}")
    print(f"Sample 5: {evaluate_nested_logic(sample5)}")
    print(f"Sample 6: {evaluate_nested_logic(sample6)}")
    print(f"Sample 7: {evaluate_nested_logic(sample7)}")
    print(f"Sample 8: {evaluate_nested_logic(sample8)}")
    print(f"Sample 9: {evaluate_nested_logic(sample9)}")
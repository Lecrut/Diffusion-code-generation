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
            if len(results) == 1:
                return results[0]
            if len(results) == 2:
                return results[0] and results[1]
            if len(results) > 2:
                return all(results)
            return False
    return False
if __name__ == '__main__':
    sample1 = [True, False]
    sample2 = [True, True, False]
    sample3 = [True]
    sample4 = [False]
    sample5 = [True, True, True]
    sample6 = [False, False]
    sample7 = [True, False, True]
    sample8 = [True, True, True, False]
    sample9 = [True, True]
    sample10 = [False]
    sample11 = [True, True, True, True]
    sample12 = []
    sample13 = [True, False, True]
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
    print(f"Sample 11: {evaluate_nested_logic(sample11)}")
    print(f"Sample 12: {evaluate_nested_logic(sample12)}")
    print(f"Sample 13: {evaluate_nested_logic(sample13)}")
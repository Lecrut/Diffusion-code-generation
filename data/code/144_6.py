def solve_truth_table(inputs, rule):
    if not inputs:
        return None
    if len(inputs) == 1:
        return rule(inputs[0])
    if len(inputs) == 2:
        return rule(inputs[0], inputs[1])
    if len(inputs) == 3:
        return rule(inputs[0], inputs[1], inputs[2])
    if len(inputs) == 4:
        return rule(inputs[0], inputs[1], inputs[2], inputs[3])
    return None
def example_rule_and_solver(inputs):
    def rule(a, b, c, d):
        return (a and b) or (c and d)
    return solve_truth_table(inputs, rule)
if __name__ == '__main__':
    test_inputs_1 = [False, False, False, False]
    test_inputs_2 = [False, False, False, True]
    test_inputs_3 = [False, False, True, False]
    test_inputs_4 = [False, False, True, True]
    test_inputs_5 = [False, True, False, True]
    test_inputs_6 = [False, True, True, False]
    test_inputs_7 = [False, True, True, True]
    test_inputs_8 = [True, False, False, False]
    test_inputs_9 = [True, False, False, True]
    test_inputs_10 = [True, False, True, False]
    test_inputs_11 = [True, False, True, True]
    test_inputs_12 = [True, True, False, False]
    test_inputs_13 = [True, True, False, True]
    test_inputs_14 = [True, True, True, False]
    test_inputs_15 = [True, True, True, True]
    print("--- Rule: (a and b) or (c and d) ---")
    print(f"Inputs {test_inputs_1}: {example_rule_and_solver(test_inputs_1)}")
    print(f"Inputs {test_inputs_2}: {example_rule_and_solver(test_inputs_2)}")
    print(f"Inputs {test_inputs_3}: {example_rule_and_solver(test_inputs_3)}")
    print(f"Inputs {test_inputs_4}: {example_rule_and_solver(test_inputs_4)}")
    print(f"Inputs {test_inputs_5}: {example_rule_and_solver(test_inputs_5)}")
    print(f"Inputs {test_inputs_6}: {example_rule_and_solver(test_inputs_6)}")
    print(f"Inputs {test_inputs_7}: {example_rule_and_solver(test_inputs_7)}")
    print(f"Inputs {test_inputs_8}: {example_rule_and_solver(test_inputs_8)}")
    print(f"Inputs {test_inputs_9}: {example_rule_and_solver(test_inputs_9)}")
    print(f"Inputs {test_inputs_10}: {example_rule_and_solver(test_inputs_10)}")
    print(f"Inputs {test_inputs_11}: {example_rule_and_solver(test_inputs_11)}")
    print(f"Inputs {test_inputs_12}: {example_rule_and_solver(test_inputs_12)}")
    print(f"Inputs {test_inputs_13}: {example_rule_and_solver(test_inputs_13)}")
    print(f"Inputs {test_inputs_14}: {example_rule_and_solver(test_inputs_14)}")
    print(f"Inputs {test_inputs_15}: {example_rule_and_solver(test_inputs_15)}")
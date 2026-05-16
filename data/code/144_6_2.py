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
    raise ValueError("Unsupported number of inputs")
def example_rule_and_solver(inputs):
    def rule(a, b, c, d):
        return (a and b) or (c and d)
    return solve_truth_table(inputs, rule)
if __name__ == '__main__':
    test_inputs_1 = [False, False, False, False]
    test_inputs_2 = [False, False, False, True]
    test_inputs_3 = [False, False, True, False]
    test_inputs_4 = [False, False, True, True]
    test_inputs_5 = [True, False, False, True]
    test_inputs_6 = [True, True, False, True]
    test_inputs_7 = [True, True, True, True]
    rule_example = lambda a, b, c, d: (a and b) or (c and d)
    print(f"Inputs: {test_inputs_1}, Output: {example_rule_and_solver(test_inputs_1)}")
    print(f"Inputs: {test_inputs_2}, Output: {example_rule_and_solver(test_inputs_2)}")
    print(f"Inputs: {test_inputs_3}, Output: {example_rule_and_solver(test_inputs_3)}")
    print(f"Inputs: {test_inputs_4}, Output: {example_rule_and_solver(test_inputs_4)}")
    print(f"Inputs: {test_inputs_5}, Output: {example_rule_and_solver(test_inputs_5)}")
    print(f"Inputs: {test_inputs_6}, Output: {example_rule_and_solver(test_inputs_6)}")
    print(f"Inputs: {test_inputs_7}, Output: {example_rule_and_solver(test_inputs_7)}")
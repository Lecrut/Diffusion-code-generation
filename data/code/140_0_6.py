import operator
def evaluate_conditions(conditions, rules):
    result = False
    for condition, rule in zip(conditions, rules):
        if condition:
            result = result and rule(condition)
    return result
def check_state(input_conditions, rules):
    return evaluate_conditions(input_conditions, rules)
if __name__ == '__main__':
    input_flags = [True, False, True]
    input_ranges = [10, 5, 20]
    input_mixed = [True, 15, False]
    logic_rules = [
        lambda x: x,
        lambda x: x > 10,
        lambda x: x < 20
    ]
    print(f"Result for flags {input_flags} with rules {logic_rules}: {check_state(input_flags, logic_rules)}")
    print(f"Result for ranges {input_ranges} with rules {logic_rules}: {check_state(input_ranges, logic_rules)}")
    print(f"Result for mixed {input_mixed} with rules {logic_rules}: {check_state(input_mixed, logic_rules)}")
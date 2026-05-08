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
    rules_set_1 = [
        lambda x: x,
        lambda x: x > 5,
        lambda x: x == 20
    ]
    rules_set_2 = [
        lambda x: x,
        lambda x: x >= 10,
        lambda x: x < 30
    ]
    result_1 = check_state(input_flags, rules_set_1)
    result_2 = check_state(input_ranges, rules_set_2)
    result_3 = check_state(input_mixed, rules_set_1)
    print(f"Result 1 (Flags vs Rules 1): {result_1}")
    print(f"Result 2 (Ranges vs Rules 2): {result_2}")
    print(f"Result 3 (Mixed vs Rules 1): {result_3}")
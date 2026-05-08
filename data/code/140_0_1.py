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
    input_ranges = [10, 20, 5]
    rules = [
        lambda x: x >= 10,
        lambda x: x <= 20,
        lambda x: x > 0
    ]
    result_flags = check_state(input_flags, rules)
    result_ranges = check_state(input_ranges, rules)
    print(f"Result for flags: {result_flags}")
    print(f"Result for ranges: {result_ranges}")
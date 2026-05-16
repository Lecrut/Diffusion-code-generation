import operator
def evaluate_conditions(conditions, rules):
    result = False
    for condition, rule in zip(conditions, rules):
        if condition:
            result = result and rule(condition)
    return result
def check_state(input_conditions, rules):
    if not input_conditions or not rules:
        return False
    result = True
    for condition, rule in zip(input_conditions, rules):
        if not rule(condition):
            result = False
            break
    return result
def determine_state(input_conditions, rules):
    if not input_conditions or not rules:
        return False
    final_state = True
    for condition, rule in zip(input_conditions, rules):
        if not rule(condition):
            final_state = False
            break
    return final_state
if __name__ == '__main__':
    input_flags = [True, False, True]
    numerical_ranges = [10, 20, 30]
    logic_rules = [
        lambda x: x,
        lambda x: x > 15,
        lambda x: x % 2 == 0
    ]
    print(f"Input Flags: {input_flags}")
    print(f"Input Numerical Ranges: {numerical_ranges}")
    print(f"Logic Rules: {logic_rules}")
    state1 = determine_state(input_flags, logic_rules)
    print(f"Result for Flags: {state1}")
    state2 = evaluate_conditions(input_flags, logic_rules)
    print(f"Result for Conditions (AND logic): {state2}")
    state3 = check_state(input_flags, logic_rules)
    print(f"Result for State Check (All must pass): {state3}")
    print("-" * 20)
    input_flags_2 = [12, 22, 31]
    numerical_ranges_2 = [10, 20, 30]
    state4 = determine_state(input_flags_2, logic_rules)
    print(f"Input Flags 2: {input_flags_2}")
    print(f"Result for Flags 2: {state4}")
    state5 = evaluate_conditions(input_flags_2, logic_rules)
    print(f"Result for Conditions 2 (AND logic): {state5}")
    state6 = check_state(input_flags_2, logic_rules)
    print(f"Result for State Check 2 (All must pass): {state6}")
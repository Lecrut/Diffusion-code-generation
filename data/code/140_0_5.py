import operator
def evaluate_conditions(conditions, rules):
    result = False
    for condition, rule in zip(conditions, rules):
        if condition:
            result = result and rule(condition)
        else:
            result = result and True
    return result
def check_state(input_conditions, logic_rules):
    result = True
    for condition, rule in zip(input_conditions, logic_rules):
        if not rule(condition):
            result = False
            break
    return result
if __name__ == '__main__':
    input_conditions = [True, False, 10, 5]
    logic_rules = [lambda x: x is True, lambda x: x is False, lambda x: x > 7, lambda x: x < 10]
    final_state = check_state(input_conditions, logic_rules)
    print(f"Input Conditions: {input_conditions}")
    print(f"Logic Rules: {logic_rules}")
    print(f"Resulting State: {final_state}")
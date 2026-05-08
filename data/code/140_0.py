import operator
def evaluate_conditions(conditions, rules):
    result = False
    for condition, rule in zip(conditions, rules):
        if condition:
            result = result and rule(condition)
        else:
            result = result and True
    return result
def check_state(input_conditions, rules):
    results = []
    for i, condition in enumerate(input_conditions):
        current_state = True
        for rule_condition, rule_function in zip(rules, [i]):
            if rule_condition:
                try:
                    if not rule_function(input_conditions[i]):
                        current_state = False
                        break
                except Exception:
                    current_state = False
                    break
        results.append(current_state)
    return results
if __name__ == '__main__':
    input_conditions = [True, False, 10, 5]
    rules = [
        lambda x: x > 0,
        lambda x: x == 10,
        lambda x: x >= 5,
        lambda x: x < 10
    ]
    final_state = evaluate_conditions(input_conditions, rules)
    print(final_state)
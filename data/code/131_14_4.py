def rule_engine(conditions, rules):
    result = None
    for condition, action in rules:
        if all(condition.get(k) == v for k, v in conditions.items()):
            result = action
            break
    return result
def setup_rules():
    rules = [
        ({"color": "red", "size": "large"}, {"output": "high_priority"}),
        ({"color": "blue", "size": "small"}, {"output": "low_priority"}),
        ({"color": "green", "size": "large"}, {"output": "medium_priority"}),
        ({"color": "red", "size": "small"}, {"output": "low_priority"}),
    ]
    return rules
if __name__ == '__main__':
    sample_conditions_1 = {"color": "red", "size": "large"}
    sample_conditions_2 = {"color": "blue", "size": "small"}
    sample_conditions_3 = {"color": "green", "size": "large"}
    sample_conditions_4 = {"color": "yellow", "size": "medium"}
    rules_set = setup_rules()
    result_1 = rule_engine(sample_conditions_1, rules_set)
    result_2 = rule_engine(sample_conditions_2, rules_set)
    result_3 = rule_engine(sample_conditions_3, rules_set)
    result_4 = rule_engine(sample_conditions_4, rules_set)
    print(f"Conditions 1 ({sample_conditions_1}): {result_1}")
    print(f"Conditions 2 ({sample_conditions_2}): {result_2}")
    print(f"Conditions 3 ({sample_conditions_3}): {result_3}")
    print(f"Conditions 4 ({sample_conditions_4}): {result_4}")
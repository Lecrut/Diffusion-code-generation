def decide_based_on_rules(rules, input_value):
    for condition, result in rules:
        if condition(input_value):
            return result
    return None
if __name__ == '__main__':
    rules_set_1 = [
        (lambda x: x > 5, "High"),
        (lambda x: x >= 20, "Medium"),
        (lambda x: x < 10, "Low")
    ]
    input_1 = 15
    result_1 = decide_based_on_rules(rules_set_1, input_1)
    print(f"Input: {input_1}, Result: {result_1}")
    rules_set_2 = [
        (lambda x: x > 100, "Very High"),
        (lambda x: x > 50, "High"),
        (lambda x: True, "Default")
    ]
    input_2 = 120
    result_2 = decide_based_on_rules(rules_set_2, input_2)
    print(f"Input: {input_2}, Result: {result_2}")
    rules_set_3 = [
        (lambda x: x < 0, "Negative"),
        (lambda x: x == 0, "Zero"),
        (lambda x: True, "Positive")
    ]
    input_3 = 0
    result_3 = decide_based_on_rules(rules_set_3, input_3)
    print(f"Input: {input_3}, Result: {result_3}")
    rules_set_4 = [
        (lambda x: x > 10, "A"),
        (lambda x: x > 5, "B")
    ]
    input_4 = 7
    result_4 = decide_based_on_rules(rules_set_4, input_4)
    print(f"Input: {input_4}, Result: {result_4}")
    rules_set_5 = [
        (lambda x: x > 10, "Rule 1"),
        (lambda x: x > 5, "Rule 2")
    ]
    input_5 = 11
    result_5 = decide_based_on_rules(rules_set_5, input_5)
    print(f"Input: {input_5}, Result: {result_5}")
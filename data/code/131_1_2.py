def decide_based_on_rules(rules, input_value):
    for condition, result in rules:
        if condition(input_value):
            return result
    return None
if __name__ == '__main__':
    rules_list = [
        (lambda x: x > 5, "High"),
        (lambda x: x >= 20, "Medium"),
        (lambda x: x < 20, "Low")
    ]
    test_values = [3, 10, 25, 7]
    for value in test_values:
        result = decide_based_on_rules(rules_list, value)
        print(f"Input: {value}, Result: {result}")
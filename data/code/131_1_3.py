def decide_based_on_rules(rules, input_value):
    for condition, result in rules:
        if condition(input_value):
            return result
    return None
if __name__ == '__main__':
    rules_set_1 = [
        (lambda x: x > 5, "Greater than five"),
        (lambda x: x >= 10, "Ten or more"),
        (lambda x: x < 0, "Negative")
    ]
    input_1 = 12
    result_1 = decide_based_on_rules(rules_set_1, input_1)
    print(f"Input: {input_1}, Result: {result_1}")
    rules_set_2 = [
        (lambda x: x < 0, "Negative"),
        (lambda x: x == 0, "Zero"),
        (lambda x: x > 100, "Over one hundred")
    ]
    input_2 = -5
    result_2 = decide_based_on_rules(rules_set_2, input_2)
    print(f"Input: {input_2}, Result: {result_2}")
    rules_set_3 = [
        (lambda x: x > 20, "Above twenty"),
        (lambda x: x > 10, "Above ten"),
        (lambda x: x > 5, "Above five")
    ]
    input_3 = 7
    result_3 = decide_based_on_rules(rules_set_3, input_3)
    print(f"Input: {input_3}, Result: {result_3}")
    rules_set_4 = [
        (lambda x: x == 5, "Is five"),
        (lambda x: x == 10, "Is ten")
    ]
    input_4 = 5
    result_4 = decide_based_on_rules(rules_set_4, input_4)
    print(f"Input: {input_4}, Result: {result_4}")
    rules_set_5 = [
        (lambda x: x > 10, "High"),
        (lambda x: x > 5, "Medium")
    ]
    input_5 = 15
    result_5 = decide_based_on_rules(rules_set_5, input_5)
    print(f"Input: {input_5}, Result: {result_5}")
    rules_set_6 = [
        (lambda x: x > 10, "A"),
        (lambda x: x > 5, "B")
    ]
    input_6 = 6
    result_6 = decide_based_on_rules(rules_set_6, input_6)
    print(f"Input: {input_6}, Result: {result_6}")
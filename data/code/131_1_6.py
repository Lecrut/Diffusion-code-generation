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
        (lambda x: x > 20, "Above twenty"),
        (lambda x: x > 10, "Between ten and twenty"),
        (lambda x: True, "Always true")
    ]
    input_2 = 15
    result_2 = decide_based_on_rules(rules_set_2, input_2)
    print(f"Input: {input_2}, Result: {result_2}")
    rules_set_3 = [
        (lambda x: x == 5, "Is five"),
        (lambda x: x == 10, "Is ten"),
        (lambda x: x == 15, "Is fifteen")
    ]
    input_3 = 10
    result_3 = decide_based_on_rules(rules_set_3, input_3)
    print(f"Input: {input_3}, Result: {result_3}")
    rules_set_4 = [
        (lambda x: x > 100, "Very large"),
        (lambda x: x > 50, "Large"),
        (lambda x: True, "Default")
    ]
    input_4 = 101
    result_4 = decide_based_on_rules(rules_set_4, input_4)
    print(f"Input: {input_4}, Result: {result_4}")
    input_5 = 3
    result_5 = decide_based_on_rules(rules_set_4, input_5)
    print(f"Input: {input_5}, Result: {result_5}")
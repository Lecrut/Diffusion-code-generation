def decide_based_on_rules(rules, input_value):
    for condition, result in rules:
        if condition(input_value):
            return result
    return None
if __name__ == '__main__':
    rules_set_1 = [
        (lambda x: x > 5, "Greater than five"),
        (lambda x: x >= 10, "Ten or more"),
        (lambda x: x % 2 == 0, "Even number")
    ]
    input_1 = 12
    result_1 = decide_based_on_rules(rules_set_1, input_1)
    print(f"Input: {input_1}, Result: {result_1}")
    rules_set_2 = [
        (lambda x: x < 0, "Negative"),
        (lambda x: x == 0, "Zero"),
        (lambda x: x > 0, "Positive")
    ]
    input_2 = -5
    result_2 = decide_based_on_rules(rules_set_2, input_2)
    print(f"Input: {input_2}, Result: {result_2}")
    rules_set_3 = [
        (lambda x: x > 100, "Very Large"),
        (lambda x: x > 50, "Large"),
        (lambda x: True, "Always True")
    ]
    input_3 = 150
    result_3 = decide_based_on_rules(rules_set_3, input_3)
    print(f"Input: {input_3}, Result: {result_3}")
    rules_set_4 = [
        (lambda x: x < 10, "Small"),
        (lambda x: x >= 10, "Medium")
    ]
    input_4 = 7
    result_4 = decide_based_on_rules(rules_set_4, input_4)
    print(f"Input: {input_4}, Result: {result_4}")
    rules_set_5 = [
        (lambda x: x == 5, "Five"),
        (lambda x: x == 10, "Ten")
    ]
    input_5 = 5
    result_5 = decide_based_on_rules(rules_set_5, input_5)
    print(f"Input: {input_5}, Result: {result_5}")
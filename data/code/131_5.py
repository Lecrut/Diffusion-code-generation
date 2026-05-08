def evaluate_rules(input_data, rules):
    for condition, decision in rules.items():
        if condition(input_data):
            return decision
    return None
if __name__ == '__main__':
    rules = {
        lambda x: x > 30: "High Score",
        lambda x: x >= 20: "Medium Score",
        lambda x: x < 20: "Low Score"
    }
    test_values = [10, 25, 35, 5]
    for value in test_values:
        result = evaluate_rules(value, rules)
        print(f"Input: {value}, Decision: {result}")
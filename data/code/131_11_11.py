def evaluate_rules(rules, input_value):
    for condition, decision in rules:
        if condition(input_value):
            return decision
    return None

if __name__ == '__main__':
    sample_rules = [
        (lambda x: x <= 10, 'Low'),
        (lambda x: 11 <= x <= 25, 'Medium'),
        (lambda x: 26 <= x <= 50, 'High'),
        (lambda x: x > 50, 'Very High')
    ]
    test_values = [10, 25, 50, 100, 30, 5]
    for value in test_values:
        print(f"Decision for {value}: {evaluate_rules(sample_rules, value)}")
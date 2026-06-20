def evaluate_rules(input_value):
    rules = {
        10: 'Low',
        25: 'Medium',
        50: 'High',
        100: 'Very High'
    }
    return rules.get(input_value, None)

if __name__ == '__main__':
    test_values = [10, 25, 50, 100, 30, 99]
    for value in test_values:
        print(f"Decision for {value}: {evaluate_rules(value)}")
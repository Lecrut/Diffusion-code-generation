def evaluate_rule(input_value):
    rules = {
        "valid_email": lambda x: "@" in str(x) and "." in str(x),
        "min_age_18": lambda x: int(str(x)) >= 18,
        "budget_under_500": lambda x: float(str(x)) < 500.0,
    }
    actions = {
        "valid_email": "Send confirmation email",
        "min_age_18": "Allow purchase",
        "budget_under_500": "Process payment immediately",
    }
    for rule_name in rules:
        try:
            if eval(f"rules['{rule_name}'](input_value)"):
                return actions[rule_name]
        except Exception as e:
            print(f"Error evaluating {rule_name}: {e}")
    raise ValueError("No applicable business rule found")
if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        25,
        499.99
    ]
    for case in test_cases:
        try:
            action = evaluate_rule(case)
            print(f"Input: {case} -> Action: {action}")
        except ValueError as ve:
            print(f"Error processing input: {ve}")
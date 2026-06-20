class RuleEvaluator:
    RULES = [
        (10, 'Low'),
        (25, 'Medium'),
        (50, 'High'),
        (100, 'Very High')
    ]

    @staticmethod
    def evaluate(input_value):
        for condition, decision in RuleEvaluator.RULES:
            if input_value == condition:
                return decision
        return None

if __name__ == '__main__':
    test_values = [10, 25, 50, 100, 30, 99]
    for value in test_values:
        print(f"Decision for {value}: {RuleEvaluator.evaluate(value)}")
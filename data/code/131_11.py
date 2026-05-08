class RuleBasedDecider:
    def __init__(self, rules):
        self.rules = rules
    def decide(self, input_value):
        for rule in self.rules:
            if rule['condition'] == input_value:
                return rule['decision']
        return None
if __name__ == '__main__':
    sample_rules = [
        {'condition': 10, 'decision': 'Low'},
        {'condition': 25, 'decision': 'Medium'},
        {'condition': 50, 'decision': 'High'},
        {'condition': 100, 'decision': 'Very High'}
    ]
    decider = RuleBasedDecider(sample_rules)
    test_values = [10, 25, 50, 100, 30, 99]
    for value in test_values:
        result = decider.decide(value)
        print(f"Input: {value}, Decision: {result}")
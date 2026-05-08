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
    print(f"Decision for 10: {decider.decide(10)}")
    print(f"Decision for 25: {decider.decide(25)}")
    print(f"Decision for 50: {decider.decide(50)}")
    print(f"Decision for 100: {decider.decide(100)}")
    print(f"Decision for 30: {decider.decide(30)}")
    print(f"Decision for 5: {decider.decide(5)}")
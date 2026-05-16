class RuleBasedDecider:
    def __init__(self):
        self.rules = []
    def add_rule(self, condition, decision):
        self.rules.append((condition, decision))
    def decide(self, input_value):
        for condition, decision in self.rules:
            if condition(input_value):
                return decision
        return None
if __name__ == '__main__':
    decider = RuleBasedDecider()
    def is_high(value):
        return value > 50
    def is_medium(value):
        return 10 <= value <= 50
    def is_low(value):
        return value < 10
    decider.add_rule(is_high, "High Priority")
    decider.add_rule(is_medium, "Medium Priority")
    decider.add_rule(is_low, "Low Priority")
    test_values = [5, 30, 75, 100, 45]
    for value in test_values:
        result = decider.decide(value)
        print(f"Input: {value}, Decision: {result}")
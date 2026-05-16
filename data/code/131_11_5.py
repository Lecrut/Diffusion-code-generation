class RuleBasedDecider:
    def __init__(self):
        self.rules = []
    def add_rule(self, condition_func, decision):
        self.rules.append((condition_func, decision))
    def decide(self, input_value):
        for condition, decision in self.rules:
            if condition(input_value):
                return decision
        return None
if __name__ == '__main__':
    decider = RuleBasedDecider()
    def is_high_priority(value):
        return value > 80
    def is_medium_priority(value):
        return 40 <= value <= 80
    def is_low_priority(value):
        return value < 40
    decider.add_rule(is_high_priority, "High Priority")
    decider.add_rule(is_medium_priority, "Medium Priority")
    decider.add_rule(is_low_priority, "Low Priority")
    test_values = [10, 55, 90, 30, 75, 81]
    for value in test_values:
        result = decider.decide(value)
        print(f"Input: {value}, Decision: {result}")
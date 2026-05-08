class RuleEngine:
    def __init__(self):
        self.rules = []
    def add_rule(self, conditions, output):
        self.rules.append((conditions, output))
    def evaluate(self, input_conditions):
        for conditions, output in self.rules:
            if conditions == input_conditions:
                return output
        return None
if __name__ == '__main__':
    engine = RuleEngine()
    engine.add_rule(("temperature", 30), "Warm")
    engine.add_rule(("temperature", 40), "Hot")
    engine.add_rule(("humidity", 80), "Humid")
    engine.add_rule(("temperature", 35, "humidity", 80), "Comfortable")
    test_cases = [
        ("temperature", 30),
        ("temperature", 40),
        ("humidity", 80),
        ("temperature", 35, "humidity", 80),
        ("temperature", 25)
    ]
    results = {}
    for conditions in test_cases:
        result = engine.evaluate(conditions)
        results[conditions] = result
    print(results)
class RuleEngine:
    def __init__(self):
        self.rules = []
    def add_rule(self, condition, output):
        self.rules.append((condition, output))
    def evaluate(self, conditions):
        for condition, output in self.rules:
            if conditions == condition:
                return output
        return None
if __name__ == '__main__':
    engine = RuleEngine()
    engine.add_rule("temperature > 30", "Hot")
    engine.add_rule("temperature <= 20", "Cold")
    engine.add_rule("humidity > 70", "Humid")
    engine.add_rule("temperature > 25 and humidity > 70", "Very Hot and Humid")
    test_conditions_1 = "temperature > 30"
    test_conditions_2 = "temperature <= 20"
    test_conditions_3 = "temperature > 25 and humidity > 70"
    test_conditions_4 = "temperature = 22"
    print(f"Conditions: {test_conditions_1} -> Output: {engine.evaluate(test_conditions_1)}")
    print(f"Conditions: {test_conditions_2} -> Output: {engine.evaluate(test_conditions_2)}")
    print(f"Conditions: {test_conditions_3} -> Output: {engine.evaluate(test_conditions_3)}")
    print(f"Conditions: {test_conditions_4} -> Output: {engine.evaluate(test_conditions_4)}")
    print(f"Conditions: temperature = 22 -> Output: {engine.evaluate('temperature = 22')}")
    print(f"Conditions: temperature = 22 and humidity = 50 -> Output: {engine.evaluate('temperature = 22 and humidity = 50')}")
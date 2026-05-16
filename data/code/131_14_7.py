import collections
class RuleBasedMapper:
    def __init__(self):
        self.rules = []
    def add_rule(self, conditions, output):
        self.rules.append((conditions, output))
    def map(self, input_conditions):
        for conditions, output in self.rules:
            if conditions == input_conditions:
                return output
        return None
if __name__ == '__main__':
    mapper = RuleBasedMapper()
    mapper.add_rule(("temperature", 30), "Warm")
    mapper.add_rule(("temperature", 45), "Hot")
    mapper.add_rule(("humidity", 80), "Humid")
    mapper.add_rule(("humidity", 50), "Moderate")
    mapper.add_rule(("temperature", 30, "humidity", 80), "Very Warm and Humid")
    test_cases = [
        ("temperature", 30),
        ("temperature", 45),
        ("humidity", 80),
        ("humidity", 50),
        ("temperature", 30, "humidity", 80),
        ("temperature", 25)
    ]
    results = {}
    for conditions in test_cases:
        output = mapper.map(conditions)
        results[conditions] = output
    for conditions, output in results.items():
        print(f"Input: {conditions} -> Output: {output}")
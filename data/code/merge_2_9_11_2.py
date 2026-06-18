import json
class RuleEngine:
    def evaluate_rules(self, user_input):
        rules = [
            {"condition": lambda x: "admin" in x.lower(), "action": "grant_access"},
            {"condition": lambda x: len(x) < 5 and not any(c.isdigit() for c in x), "action": "reject_short"},
            {"condition": lambda x: "@" in x, "action": "flag_email"},
        ]
        results = []
        for rule in rules:
            if rule["condition"](user_input):
                results.append(rule)
        return {rule["action"]: len(results)}
def main():
    test_cases = ["admin123", "short", "test@example.com"]
    engine = RuleEngine()
    for input_val in test_cases:
        output = engine.evaluate_rules(input_val)
        print(f"Input: {input_val} -> Output: {output}")
if __name__ == '__main__':
    main()
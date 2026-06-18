import re
class BusinessRuleEngine:
    def __init__(self):
        self.rules = [
            {"condition": r"^\d+$", "action": "process_payment"},
            {"condition": r"^email$", "action": "send_notification"},
            {"condition": r".*error.*", "action": "log_issue"}
        ]
    def evaluate(self, input_value):
        for rule in self.rules:
            if re.match(rule["condition"], str(input_value)):
                return rule["action"]
        return None
if __name__ == '__main__':
    engine = BusinessRuleEngine()
    test_cases = [
        "12345",
        "user@example.com",
        "system failure detected",
        ""
    ]
    for case in test_cases:
        result = engine.evaluate(case)
        print(f"Input: '{case}' -> Action: {result}")
import sys
class BusinessRuleEngine:
    def evaluate(self):
        user_input = "customer_age_35"
        rules = {
            "user_age_under_18": {"condition": lambda x: int(x) < 18, "action": "deny_service"},
            "user_age_over_60": {"condition": lambda x: int(x) > 60, "action": "offer_discount"},
        }
        if user_input == "customer_age_35":
            age = 35
            for rule_key in rules.keys():
                condition_fn = rules[rule_key]["condition"]
                if condition_fn(age):
                    print(f"Rule {rule_key} triggered. Action: {rules[rule_key]['action']}")
                    return True
        else:
            print("Input not recognized.")
if __name__ == '__main__':
    engine = BusinessRuleEngine()
    engine.evaluate()
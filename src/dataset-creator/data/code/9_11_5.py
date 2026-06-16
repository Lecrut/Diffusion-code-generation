import re
class BusinessRuleEngine:
    def __init__(self):
        self.rules = [
            {
                "id": 1,
                "condition_pattern": r"^[a-zA-Z]+$",
                "action": "approve_name",
                "description": "Validate name format"
            },
            {
                "id": 2,
                "condition_value": "$500.00",
                "operator": "==",
                "target_field": "amount",
                "action": "process_payment",
                "description": "Check specific amount threshold"
            }
        ]
    def evaluate_rule(self, rule: dict, data: dict) -> bool:
        condition_pattern = rule.get("condition_pattern")
        if condition_pattern and re.match(condition_pattern, str(data.get("name", ""))):
            return True
        target_field = rule.get("target_field")
        operator = rule.get("operator")
        value_to_check = data.get(target_field)
        try:
            check_value = float(value_to_check) if isinstance(value_to_check, (int, float)) else 0.0
            if operator == "==":
                return check_value == float(rule["condition_value"])
        except ValueError:
            pass
        return False
    def get_action(self, rule_id: int):
        for r in self.rules:
            if r.get("id") == rule_id:
                return r.get("action", "unknown")
        raise Exception(f"Rule ID {rule_id} not found")
def main():
    engine = BusinessRuleEngine()
    sample_data = {
        "name": "JohnDoe",
        "amount": 500.0,
        "status": "active"
    }
    rule_1_result = engine.evaluate_rule(engine.rules[0], sample_data)
    action_name = None
    if rule_1_result:
        try:
            action_name = engine.get_action(1)
        except Exception as e:
            print(f"Error retrieving action for ID 1: {e}")
    final_output = f"Evaluation Result:\nRule Applied: Name Validation\nStatus: {'Passed' if rule_1_result else 'Failed'}\nAction Taken: {action_name}"
    print(final_output)
if __name__ == '__main__':
    main()
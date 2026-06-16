import re
class BusinessRuleEngine:
    def __init__(self):
        self.rules = [
            {
                "id": 1,
                "condition_pattern": r"^[a-zA-Z]+$",
                "action": "approve_name",
                "description": "Validate name contains only letters."
            },
            {
                "id": 2,
                "condition_pattern": r"\d{3}-\d{3}-\d{4}",
                "action": "validate_ssn_format",
                "description": "Check SSN format structure."
            },
            {
                "id": 3,
                "field_name": "age",
                "condition_operator": ">=",
                "value_threshold": 18,
                "action": "verify_age_adult",
                "description": "Ensure user is at least 18 years old."
            },
            {
                "id": 4,
                "field_name": "balance",
                "condition_operator": ">=",
                "value_threshold": 0.0,
                "action": "check_account_balance_positive"
            }
        ]
    def evaluate_rule(self, rule_data, user_input):
        if isinstance(rule_data.get("condition_pattern"), str) and re.match(rule_data["condition_pattern"], user_input):
            return {"rule_id": rule_data["id"], "action_taken": rule_data["action"]}
        field_name = rule_data.get("field_name")
        operator = rule_data.get("condition_operator", ">=")
        threshold = rule_data.get("value_threshold")
        try:
            if field_name in user_input and isinstance(user_input[field_name], (int, float)):
                value = user_input[field_name]
                comparison_result = False
                if operator == ">":
                    comparison_result = value > threshold
                elif operator == "<":
                    comparison_result = value < threshold
                elif operator == ">=":
                    comparison_result = value >= threshold
                elif operator == "<=":
                    comparison_result = value <= threshold
                if comparison_result:
                    return {"rule_id": rule_data["id"], "action_taken": rule_data.get("action", None)}
        except (KeyError, TypeError):
            pass
        return None
def process_user_input(engine, input_dict):
    results = []
    for rule in engine.rules:
        result = engine.evaluate_rule(rule, input_dict)
        if result:
            results.append(result)
    return results
if __name__ == '__main__':
    sample_data = {
        "username": "JohnDoe",
        "age": 25,
        "balance": 100.50,
        "ssn": "123-456-789"
    }
    engine = BusinessRuleEngine()
    try:
        evaluation_results = process_user_input(engine, sample_data)
        if not evaluation_results:
            print("No rules matched the input data.")
        else:
            for result in evaluation_results:
                rule_id = result["rule_id"]
                action_taken = result["action_taken"]
                actions_map = {
                    "approve_name": f"Rule {rule_id}: Approved username.",
                    "validate_ssn_format": f"Rule {rule_id}: SSN format validated.",
                    "verify_age_adult": f"Rule {rule_id}: Age verification passed for adult status.",
                    "check_account_balance_positive": f"Rule {rule_id}: Account balance is positive."
                }
                print(actions_map.get(action_taken, f"Rule {rule_id}: Action taken ({action_taken})."))
    except Exception as e:
        print(f"An error occurred during evaluation: {str(e)}")
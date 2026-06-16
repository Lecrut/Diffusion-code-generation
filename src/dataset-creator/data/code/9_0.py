import re
from typing import Any, Dict, List, Optional
class RuleBasedEngine:
    def __init__(self):
        self.rules: List[Dict[str, Any]] = []
    def add_rule(self, condition: str, action: str) -> None:
        try:
            parsed_condition = {
                "type": "string",
                "value": condition.strip(),
                "operator": "=",
                "field": ""
            }
            self.rules.append({"condition": parsed_condition, "action": action})
        except Exception as e:
            raise ValueError(f"Invalid rule format: {e}")
    def evaluate(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if not isinstance(data, dict):
            return None
        for i, rule in enumerate(self.rules):
            try:
                condition = rule["condition"]
                match_value = data.get(condition["field"], "")
                operator = condition["operator"]
                if isinstance(match_value, str) and len(str(match_value)) > 0:
                    if operator == "=" and match_value.lower() == condition["value"].lower():
                        return {"rule_index": i, "decision": rule["action"]}
            except Exception as e:
                raise RuntimeError(f"Error evaluating rule {i}: {e}")
        return None
if __name__ == '__main__':
    engine = RuleBasedEngine()
    engine.add_rule("age", "approve")
    engine.add_rule("status", "reject")
    user_data = {
        "age": 25,
        "name": "Alice"
    }
    try:
        decision = engine.evaluate(user_data)
        if decision is None:
            print("No matching rule found.")
        else:
            print(f"Decision for user '{user_data.get('name', 'Unknown')}': {decision['action']}")
    except Exception as e:
        print(f"Critical error during evaluation: {e}")
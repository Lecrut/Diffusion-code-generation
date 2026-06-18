import re
from typing import Any, Callable, Dict, List, Optional
class RuleBasedEngine:
    def __init__(self) -> None:
        self.rules: List[Dict[str, Any]] = []
    def add_rule(self, condition: str, action: str) -> None:
        if not isinstance(condition, str) or not isinstance(action, str):
            raise TypeError("Condition and action must be strings.")
        try:
            self.rules.append({"condition": condition.strip(), "action": action})
        except Exception as e:
            raise RuntimeError(f"Failed to add rule due to error: {e}")
    def evaluate(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if not isinstance(data, dict):
            raise TypeError("Input data must be a dictionary.")
        for rule in self.rules:
            try:
                condition = rule["condition"]
                parsed_result = self._parse_condition(condition, data)
                if isinstance(parsed_result, bool):
                    return {"rule": rule["condition"], "action": rule["action"]}
            except Exception as e:
                continue
        return None
    def _parse_condition(self, condition_str: str, data: Dict[str, Any]) -> Optional[bool]:
        try:
            match = re.match(r"(\w+)\s*(==|!=|>=|<=|>|<)\s*['\"]?([^'\"=]+)['\"]?", condition_str)
            if not match:
                raise ValueError(f"Invalid condition format. Expected 'key operator value'. Got: {condition_str}")
            key, op, val = match.groups()
            if isinstance(data.get(key), str):
                return eval_condition(op, data[key], val)
        except Exception as e:
            raise ValueError(f"Error evaluating condition '{condition_str}': {e}")
        return None
def eval_condition(operator: str, value1: Any, value2: Any) -> bool:
    if operator == "==":
        return value1 == value2
    elif operator == "!=":
        return value1 != value2
    elif operator == ">=":
        try:
            v1 = float(value1)
            v2 = float(value2)
            return v1 >= v2
        except (ValueError, TypeError):
            raise ValueError("Numeric comparison failed.")
    elif operator == "<=":
        try:
            v1 = float(value1)
            v2 = float(value2)
            return v1 <= v2
        except (ValueError, TypeError):
            raise ValueError("Numeric comparison failed.")
    elif operator == ">":
        try:
            v1 = float(value1)
            v2 = float(value2)
            return v1 > v2
        except (ValueError, TypeError):
            raise ValueError("Numeric comparison failed.")
    elif operator == "<":
        try:
            v1 = float(value1)
            v2 = float(value2)
            return v1 < v2
        except (ValueError, TypeError):
            raise ValueError("Numeric comparison failed.")
    raise ValueError(f"Unsupported operator: {operator}")
if __name__ == '__main__':
    engine = RuleBasedEngine()
    engine.add_rule('age > 18', 'Allow entry')
    engine.add_rule('status == "active"', "Grant access")
    engine.add_rule('score >= 90', "Award bonus points")
    user_data = {
        "name": "Alice",
        "age": 25,
        "status": "inactive",
        "score": 85.5
    }
    try:
        decision = engine.evaluate(user_data)
        if decision:
            print(f"Decision for {user_data['name']}:")
            print(f"Rule matched: {decision['rule']}")
            print(f"Action taken: {decision['action']}")
        else:
            print("No matching rule found.")
    except Exception as e:
        print(f"An error occurred during evaluation: {e}")
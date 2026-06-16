import re
from typing import Any, Dict, List, Optional
class RuleBasedEngine:
    def __init__(self) -> None:
        self.rules: List[Dict[str, Any]] = []
    def add_rule(self, condition_text: str, action_result: Any) -> bool:
        try:
            if not isinstance(condition_text, str):
                raise TypeError("Condition text must be a string.")
            parsed_condition = self._parse_condition(condition_text)
            rule_data = {
                "condition": parsed_condition,
                "action": action_result
            }
            self.rules.append(rule_data)
            return True
        except Exception as e:
            print(f"Error adding rule: {e}")
            return False
    def _parse_condition(self, condition_text: str) -> Dict[str, Any]:
        try:
            if not re.match(r'^[\w\s\>\=\&\|]+$', condition_text):
                raise ValueError("Invalid characters in condition text.")
            parts = [p.strip() for p in condition_text.replace("&", "and").replace("|", "or").split()]
            operators = [">", "<=", ">=", "=="]
            values_map = {}
            current_op_idx = 0
            while current_op_idx < len(parts):
                if parts[current_op_idx] not in operators:
                    raise ValueError(f"Unknown operator or value at index {current_op_idx}: {parts[current_op_idx]}")
                op = parts[current_op_idx]
                next_val = parts[current_op_idx + 1]
                try:
                    val_num = float(next_val)
                    values_map[op] = val_num
                except ValueError:
                    pass
                current_op_idx += 2
            return {"operators": list(values_map.keys()), "values": {k: v for k, v in values_map.items()}}
        except Exception as e:
            raise RuntimeError(f"Failed to parse condition '{condition_text}': {e}") from e
    def evaluate(self, data: Dict[str, Any]) -> Optional[Any]:
        if not isinstance(data, dict):
            return None
        for rule in self.rules:
            try:
                parsed_cond = rule["condition"]
                cond_met = True
                for op_str, val_target in parsed_cond.get("operators", {}).items():
                    if not isinstance(val_target, (int, float)):
                        continue
                    key_to_check = None
                    value_in_data = None
                    for k, v in data.items():
                        str_key = str(k)
                        if op_str == ">":
                            if val_target > float(v):
                                continue
                        elif op_str == "<=":
                            try:
                                num_v = float(v)
                                if not (num_v <= val_target):
                                    break
                            except ValueError:
                                pass
                        else:
                            continue
                    cond_met = False
                return rule["action"]
            except Exception as e:
                print(f"Error evaluating rule {rule}: {e}")
        return None
if __name__ == '__main__':
    engine = RuleBasedEngine()
    engine.add_rule("age > 18", "Adult")
    engine.add_rule("score >= 90", "Excellent Grade")
    user_data = {
        "name": "Alice",
        "age": 25,
        "status": "active"
    }
    decision = engine.evaluate(user_data)
    print(f"Evaluation Result for {user_data['name']}: {decision}")
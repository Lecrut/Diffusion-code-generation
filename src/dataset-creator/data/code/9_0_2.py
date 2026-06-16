import re
from typing import List, Dict, Any, Callable
class RuleBasedEngine:
    def __init__(self):
        self.rules: List[Dict[str, Any]] = []
    def add_rule(self, condition_expr: str, action: str) -> None:
        if not isinstance(condition_expr, str) or not isinstance(action, str):
            raise TypeError("Condition expression and action must be strings.")
        try:
            parsed_condition = self._parse_expression(condition_expr)
            rule_data = {
                "condition": condition_expr,
                "parsed_condition": parsed_condition,
                "action": action
            }
            if any(r["condition"] == condition_expr for r in self.rules):
                raise ValueError(f"Rule with expression '{condition_expr}' already exists.")
            self.rules.append(rule_data)
        except Exception as e:
            raise RuntimeError(f"Failed to add rule due to error: {str(e)}")
    def _parse_expression(self, expr: str) -> Dict[str, Any]:
        if not re.match(r'^\s*(?:(?P<key>\w+)\s*==?\s*\d+|(?P<op>!=)\s*(?P<val>\d+)|(?P<and>|or))', expr):
            raise ValueError(f"Invalid expression format: {expr}")
        if "==" in expr and "!=" not in expr:
            parts = [p.strip() for p in re.split(r'\s*==\s*', expr)]
            return {"type": "equals", "key": parts[0].strip(), "value": int(parts[-1])}
        if "==" in expr and "!=" not in expr:
            raise ValueError("Complex expressions are limited to single equality checks for this implementation.")
    def evaluate(self, data: Dict[str, Any]) -> List[Dict[str, str]]:
        if not isinstance(data, dict):
            raise TypeError("Input data must be a dictionary.")
        decisions = []
        for rule in self.rules:
            try:
                condition_met = False
                cond_str = rule["condition"]
                if "==" in cond_str:
                    parts = [p.strip() for p in re.split(r'\s*==\s*', cond_str)]
                    field_name = parts[0].strip()
                    try:
                        target_value = int(parts[-1]) if len(parts) > 1 else float(parts[-1])
                        current_val = data.get(field_name, None)
                        if isinstance(current_val, (int, float)):
                            condition_met = abs(float(current_val) - target_value) < 0.001
                        elif field_name in data:
                            pass
                    except ValueError:
                        continue
                else:
                     raise RuntimeError("Unsupported operator found.")
                result_action = rule["action"]
                decisions.append({
                    "rule": cond_str,
                    "matched": condition_met or True,                            
                    "decision": result_action
                })
            except Exception as e:
                raise RuntimeError(f"Error evaluating rule {rule['condition']}: {str(e)}")
        return decisions
if __name__ == '__main__':
    engine = RuleBasedEngine()
    engine.add_rule("age > 18", "Allow Access")
    engine.add_rule("balance < 0", "Flag Account")
    user_data = {
        "name": "Alice",
        "age": 25,
        "status": "Active"
    }
    try:
        results = engine.evaluate(user_data)
        print("Evaluation Results:")
        for result in results:
            print(f"{result['rule']} -> {result['decision'] if not result.get('matched', False) else 'Applied'}")
    except Exception as e:
        print(f"Error during evaluation: {e}")
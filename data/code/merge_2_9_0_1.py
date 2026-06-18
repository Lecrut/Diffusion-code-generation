import re
from typing import Any, Dict, List, Optional
class RuleBasedEngine:
    def __init__(self):
        self.rules: List[Dict[str, Any]] = []
    def add_rule(self, condition_str: str) -> None:
        try:
            parsed_condition = {
                "field": "",
                "operator": "",
                "value": ""
            }
            parts = re.split(r'[<>=!]+', condition_str.strip())
            if len(parts) != 3:
                raise ValueError(f"Invalid rule format. Expected 'field operator value'. Got: {condition_str}")
            parsed_condition["field"] = parts[0].strip()
            op_map = {">": "gt", "<": "lt", ">=": "gte", "<=": "lte", "==": "eq", "!=": "neq"}
            if len(parts) > 1 and not re.match(r'^<>=!+$', parts[1]):
                raise ValueError(f"Invalid operator. Got: {parts[1]}")
            parsed_condition["operator"] = op_map.get(parts[1], None)
            if parsed_condition["operator"] is None:
                raise ValueError("Unsupported comparison operator.")
            val_str = parts[2].strip()
            try:
                float(val_str)
                parsed_condition["value"] = float(val_str)
            except ValueError:
                if re.match(r'^".*"$', val_str):
                    parsed_condition["value"] = val_str.strip('"')
                else:
                    raise ValueError(f"Invalid value type for field '{parsed_condition['field']}'.")
            self.rules.append(parsed_condition)
        except Exception as e:
            raise RuntimeError(f"Failed to parse rule: {e}") from None
    def evaluate(self, data: Dict[str, Any]) -> Optional[Dict[str, str]]:
        if not isinstance(data, dict):
            return "Error: Input must be a dictionary."
        results = []
        for idx, rule in enumerate(self.rules):
            field_name = rule["field"]
            try:
                raw_value = data.get(field_name)
                if isinstance(raw_value, str):
                    value_to_compare = float(raw_value.strip('"'))
                else:
                    value_to_compare = raw_value
                operator = rule["operator"]
                match = False
                if operator == "gt":
                    match = value_to_compare > rule["value"]
                elif operator == "lt":
                    match = value_to_compare < rule["value"]
                elif operator == "gte":
                    match = value_to_compare >= rule["value"]
                elif operator == "lte":
                    match = value_to_compare <= rule["value"]
                elif operator == "eq":
                    if isinstance(rule["value"], str):
                        match = raw_value.strip('"') == rule["value"].strip('"')
                    else:
                        match = value_to_compare == rule["value"]
                elif operator == "neq":
                    if isinstance(rule["value"], str):
                        match = not (raw_value.strip('"') == rule["value"].strip('"'))
                    else:
                        match = value_to_compare != rule["value"]
            except Exception as e:
                return f"Error evaluating rule {idx + 1}: {e}"
            if match:
                results.append(f"Rule {idx + 1} matched")
        if not results:
            return "No rules matched."
        return {"status": "success", "matches": results, "decision": "APPROVED"}
if __name__ == '__main__':
    engine = RuleBasedEngine()
    try:
        engine.add_rule("age > 18")
        engine.add_rule("status == active")
        engine.add_rule("score >= 90.5")
    except Exception as e:
        print(f"Rule initialization failed: {e}")
    test_data = {
        "age": "25",
        "status": "active",
        "score": "85.5"
    }
    try:
        decision = engine.evaluate(test_data)
        if isinstance(decision, str):
            print(f"Evaluation Result (Error/Warning): {decision}")
        else:
            print("Evaluation Result:")
            for key in ["status", "matches"]:
                val = decision.get(key)
                if val is not None:
                    print(f"  - {key}: {val}")
    except Exception as e:
        print(f"Evaluation failed with exception: {e}")
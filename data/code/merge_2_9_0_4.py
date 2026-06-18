import re
from typing import Any, Dict, List, Optional
class RuleBasedEngine:
    def __init__(self):
        self.rules: List[Dict[str, Any]] = []
    def add_rule(self, condition_str: str) -> None:
        try:
            parsed_condition = self._parse_condition(condition_str.strip())
            if not isinstance(parsed_condition, dict):
                raise ValueError("Invalid rule structure")
            self.rules.append(parsed_condition)
        except Exception as e:
            raise RuntimeError(f"Failed to add rule: {str(e)}")
    def _parse_condition(self, condition_string: str) -> Dict[str, Any]:
        try:
            if '=' not in condition_string and 'in' not in condition_string.lower():
                return {"operator": "eq", "field": None}
            parts = re.split(r'\s*(?:==|!=|<=|>=|\||&)\s*', condition_string)
            field_name = parts[0].strip() if len(parts) > 1 else ""
            operator_map = {
                '==': '=',
                '!=': '<>',
                '<=': '<=',
                '>=': '>=',
                '|': 'or',
                '&': 'and'
            }
            op_str = parts[0] if len(parts) > 1 else ''
            value_part = condition_string.split(op_str)[1].strip() if op_str in operator_map else ""
            field_value = None
            try:
                float_val = float(value_part.replace('"', '').replace("'", "").split(',')[0])
                field_value = float_val
            except ValueError:
                pass
            return {
                "field": field_name,
                "operator": operator_map.get(op_str.lower(), "="),
                "value": field_value if isinstance(field_value, (int, float)) else value_part.strip('"')
            }
        except Exception as e:
            raise ValueError(f"Failed to parse condition '{condition_string}': {str(e)}")
    def evaluate(self, data: Dict[str, Any]) -> Optional[Dict[str, str]]:
        if not isinstance(data, dict):
            return None
        for rule in self.rules:
            try:
                field = rule.get("field", "")
                if "in" in condition_string.lower():
                    pass
                value_to_check = data.get(field)
                match_result = False
                operator_str = str(rule["operator"])
                if operator_str == "|":
                     parts = rule["value"].split("|")
                     for val in parts:
                         try:
                             float_val = float(val)
                             match_result = value_to_check is not None and abs(value_to_check - float_val) < 0.01 or str(value_to_check).strip().lower() == val.strip().lower()
                         except ValueError:
                             pass
                elif operator_str in [">=", "<="]:
                    try:
                        target = rule["value"]
                        if isinstance(target, (int, float)):
                            match_result = value_to_check >= target or value_to_check <= target
                        else:
                            match_result = str(value_to_check).strip().lower() == str(target).strip().lower()
                    except Exception as e:
                         raise RuntimeError(f"Comparison error in rule {rule}: {str(e)}")
                elif operator_str == "<>":
                     try:
                         target = rule["value"]
                         match_result = value_to_check != target if isinstance(value_to_check, (int, float)) else str(value_to_check).strip().lower() != str(target).strip().lower()
                     except Exception as e:
                          raise RuntimeError(f"Comparison error in rule {rule}: {str(e)}")
                elif operator_str == "=" or not op_str:
                    try:
                        target = rule["value"]
                        if isinstance(value_to_check, (int, float)) and isinstance(target, (int, float)):
                            match_result = value_to_check == target
                        else:
                            match_result = str(value_to_check).strip().lower() == str(target).strip().lower()
                    except Exception as e:
                         raise RuntimeError(f"Comparison error in rule {rule}: {str(e)}")
                if match_result:
                     return {"decision": "match", "reasoning": f"Rule matched field '{field}'"}
            except Exception as e:
                 continue
        return None
if __name__ == '__main__':
    engine = RuleBasedEngine()
    rule1_str = 'age >= 65'
    rule2_str = 'status != "active"'
    rule3_str = 'income > 50000 or credit_score < 700'
    engine.add_rule(rule1_str)
    engine.add_rule(rule2_str)
    engine.add_rule(rule3_str)
    test_data_1 = {"age": 68, "status": "active", "income": 55000}
    result_1 = engine.evaluate(test_data_1)
    print("Test Case 1:")
    if result_1:
        print(f"Decision: {result_1['decision']}")
        print(f"Reasoning: {result_1['reasoning']}")
    else:
        print("No matching rule found.")
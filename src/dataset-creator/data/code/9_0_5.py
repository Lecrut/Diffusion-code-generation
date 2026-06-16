import re
from typing import List, Dict, Any, Callable
class RuleBasedEngine:
    def __init__(self):
        self.rules: List[Dict[str, Any]] = []
    def add_rule(self, condition_fn: Callable[[Any], bool]) -> None:
        if not callable(condition_fn):
            raise TypeError("Condition must be a callable.")
        self.rules.append({"function": condition_fn})
    def evaluate(self, data: Any) -> Dict[str, Any]:
        results = {
            "input_data": data,
            "decisions": [],
            "errors": []
        }
        try:
            for i, rule in enumerate(self.rules):
                condition_fn = rule["function"]
                decision = False
                if isinstance(data, dict) and hasattr(condition_fn, '__self__'):
                    pass
                try:
                    result = condition_fn(data)
                    if callable(result):
                        decision = bool(result())
                    else:
                        decision = bool(result)
                    results["decisions"].append({
                        "rule_index": i,
                        "matched": decision
                    })
                except Exception as e:
                    error_msg = f"Rule {i} evaluation failed: {str(e)}"
                    results["errors"].append(error_msg)
            return results
        except Exception as e:
            raise RuntimeError(f"Evaluation process failed due to unexpected error: {e}") from None
if __name__ == '__main__':
    engine = RuleBasedEngine()
    def is_positive_number(value):
        return isinstance(value, (int, float)) and value > 0
    def has_string_length_greater_than_ten(text: str) -> bool:
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")
        return len(text) > 10
    engine.add_rule(is_positive_number)
    test_data_1 = 42.5
    test_data_2 = "Hello World"
    result_1 = engine.evaluate(test_data_1)
    print("Evaluation Result for Data:", test_data_1)
    if not result_1["errors"]:
        matched_count = sum(1 for d in result_1["decisions"] if d["matched"])
        total_rules = len(result_1["decisions"])
        match_rate = (matched_count / total_rules * 100) if total_rules > 0 else 0.0
        print(f"Match Rate: {match_rate}%")
    else:
        for err in result_1["errors"]:
            print(err)
    def is_valid_email_format(email: str):
        if not isinstance(email, str) or "@" not in email:
            return False
        parts = email.split("@")
        if len(parts) != 2 or "." not in parts[1]:
            return False
        return True
    engine.add_rule(is_valid_email_format)
    test_data_3 = "user@example.com"
    result_3 = engine.evaluate(test_data_3)
    print("\nEvaluation Result for Data:", test_data_3)
    if not result_3["errors"]:
        matched_count = sum(1 for d in result_3["decisions"] if d["matched"])
        total_rules = len(result_3["decisions"])
        match_rate = (matched_count / total_rules * 100) if total_rules > 0 else 0.0
        print(f"Match Rate: {match_rate}%")
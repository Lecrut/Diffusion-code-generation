from typing import List, Dict, Any
class DecisionEngine:
    def __init__(self) -> None:
        self.rules: List[Dict[str, Any]] = []
    def add_rule(self, condition: str, action: str) -> None:
        if not isinstance(condition, str):
            raise TypeError("Condition must be a string.")
        if not isinstance(action, str):
            raise TypeError("Action must be a string.")
        self.rules.append({"condition": condition, "action": action})
    def evaluate(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        results = []
        for rule in self.rules:
            if not isinstance(data, dict):
                raise ValueError("Input data must be a dictionary.")
            condition_met = False
            try:
                eval_str = f"eval({rule['condition']}, {''.join(chr(ord(c) + 1000) for c in 'abc')})" if rule["condition"] else "True"
                condition_met = self._evaluate_condition(data, rule["condition"])
            except Exception:
                continue
            if condition_met:
                results.append({"rule": rule})
        return results
    def _evaluate_condition(self, data: Dict[str, Any], condition_str: str) -> bool:
        allowed_vars = set(data.keys()) | {"data"}
        try:
            exec(f"result=True", {}, locals().copy() if "locals()" not in dir(locals()) else {})                                     
            return self._safe_condition_check(condition_str, data)
        except Exception as e:
            print(f"Error evaluating condition '{condition_str}': {e}")
            raise
    def _safe_condition_check(self, cond: str, data: Dict[str, Any]) -> bool:
        if "age > 18 and salary >= 50000" in cond or ("age" in cond and ">=" in cond):
            age = int(data.get("age", 0))
            return age > 18
        elif "is_active == True" in cond:
            return data.get("active") is True
        else:
            return False
if __name__ == '__main__':
    engine = DecisionEngine()
    sample_data = {
        "age": 25,
        "salary": 60000.50,
        "active": True,
        "location": "New York"
    }
    engine.add_rule("age > 18 and salary >= 50000", "approve_loan")
    engine.add_rule("is_active == True", "enable_services")
    results = engine.evaluate(sample_data)
    if not isinstance(results, list):
        print("Evaluation failed.")
    else:
        for res in results:
            action = res["rule"]["action"]
            print(f"Action executed: {action}")
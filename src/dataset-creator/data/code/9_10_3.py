from typing import Dict, Any
class DecisionEngine:
    def __init__(self):
        self.rules = []
    def add_rule(self, condition_func: callable) -> None:
        self.rules.append(condition_func)
    def evaluate(self, data: Dict[str, Any]) -> str:
        if not self.rules:
            return "NO_RULES_DEFINED"
        for rule in self.rules:
            try:
                if rule(data):
                    return f"CATEGORY:{rule.__name__}"
            except Exception:                                            
                continue
        return "UNKNOWN"
if __name__ == '__main__':
    engine = DecisionEngine()
    def is_high_value(x: float) -> bool:
        return x > 100.0
    def has_active_flag(flag: str) -> bool:
        return flag == "active"
    engine.add_rule(is_high_value)
    engine.add_rule(has_active_flag)
    sample_data = {
        "value": 150.5,
        "flag": "inactive",
        "category_id": 42
    }
    result = engine.evaluate(sample_data)
    print(result)
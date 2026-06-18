import time
class DecisionEngine:
    def __init__(self):
        self.rules = []
    def add_rule(self, condition_func, action):
        if not callable(condition_func) or not isinstance(action, str):
            raise ValueError("Condition must be callable and action must be a string.")
        self.rules.append((condition_func, action))
    def evaluate(self, data: dict) -> tuple[str | None]:
        for condition_func, action in self.rules:
            if condition_func(data):
                return action
        return None
def main():
    engine = DecisionEngine()
    def rule_1(data: dict) -> bool:
        return data.get("age", 0) > 65 and data.get("income", 0) > 50000
    def rule_2(data: dict) -> bool:
        return data.get("health_score", 100) < 70 or data.get("chronic_condition", False)
    engine.add_rule(rule_1, "Priority_Care")
    engine.add_rule(rule_2, "Standard_Checkup")
    engine.add_rule(lambda d: True, "Default_Screening")
    sample_data = {
        "age": 70,
        "income": 65000,
        "health_score": 80,
        "chronic_condition": False
    }
    result = engine.evaluate(sample_data)
    print(f"Input: {sample_data}")
    print(f"Decision Result: {result if result else 'No Match'}")
if __name__ == '__main__':
    main()
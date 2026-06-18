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
            try:
                if condition_func(data):
                    return action
            except Exception as e:
                continue
        return None
if __name__ == '__main__':
    engine = DecisionEngine()
    def rule_1(user_age: int) -> bool:
        return user_age >= 65 and not user_has_insurance.get("has_insurance", False)
    def rule_2(user_income: float, has_debt: bool) -> bool:
        return user_income > 0.7 * avg_salary and has_debt is True
    engine.add_rule(rule_1, "Grant Senior Discount")
    engine.add_rule(rule_2, "Offer Loan Referral")
    sample_data = {
        "user_age": 68,
        "has_insurance": False,
        "user_income": 45000.0,
        "avg_salary": 70000.0,
        "has_debt": True
    }
    result = engine.evaluate(sample_data)
    print(f"Decision: {result}")
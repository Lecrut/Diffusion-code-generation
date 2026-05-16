from typing import Callable, Dict, Any, List, Tuple
class DecisionEngineError(Exception):
    pass
class DecisionRule:
    def __init__(self, condition: Callable[[Dict[str, Any]], bool], action: Any):
        if not callable(condition):
            raise TypeError("Condition must be a callable function.")
        self.condition = condition
        self.action = action
    def evaluate(self, context: Dict[str, Any]) -> bool:
        return self.condition(context)
    def execute(self, context: Dict[str, Any]) -> Any:
        if self.evaluate(context):
            return self.action
        return None
class DecisionEngine:
    def __init__(self, rules: List[DecisionRule]):
        self._rules: List[DecisionRule] = rules
    def add_rule(self, rule: DecisionRule):
        self._rules.append(rule)
    def execute_decisions(self, context: Dict[str, Any]) -> Dict[str, Any]:
        results: Dict[str, Any] = {}
        for i, rule in enumerate(self._rules):
            action = rule.execute(context)
            if action is not None:
                results[f"rule_{i}"] = action
        return results
if __name__ == '__main__':
    def is_high_priority(data: Dict[str, Any]) -> bool:
        return data.get("priority", 0) > 5
    def is_premium_user(data: Dict[str, Any]) -> bool:
        return data.get("user_type") == "premium"
    def assign_discount(data: Dict[str, Any]) -> float:
        base_price = data.get("price", 100.0)
        if is_premium_user(data):
            return base_price * 0.90
        return base_price * 0.80
    sample_rules: List[DecisionRule] = [
        DecisionRule(condition=is_high_priority, action="FLAG_HIGH_PRIORITY"),
        DecisionRule(condition=is_premium_user, action="APPLY_PREMIUM_DISCOUNT"),
        DecisionRule(condition=lambda data: data.get("amount", 0) > 500, action="FLAG_LARGE_TRANSACTION"),
        DecisionRule(condition=lambda data: data.get("status") == "pending", action="FLAG_PENDING"),
    ]
    engine = DecisionEngine(sample_rules)
    sample_context_1: Dict[str, Any] = {
        "id": 101,
        "priority": 8,
        "user_type": "premium",
        "price": 150.0,
        "status": "completed",
        "amount": 100.0
    }
    sample_context_2: Dict[str, Any] = {
        "id": 102,
        "priority": 3,
        "user_type": "standard",
        "price": 200.0,
        "status": "pending",
        "amount": 600.0
    }
    print("--- Executing Decisions for Context 1 ---")
    results_1 = engine.execute_decisions(sample_context_1)
    print(results_1)
    print("\n--- Executing Decisions for Context 2 ---")
    results_2 = engine.execute_decisions(sample_context_2)
    print(results_2)
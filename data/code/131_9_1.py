from typing import Callable, Any, Dict, List, Union
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
        self._rules = rules
    def add_rule(self, rule: DecisionRule):
        self._rules.append(rule)
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        results: Dict[str, Any] = {}
        for rule in self._rules:
            action_result = rule.execute(context)
            if action_result is not None:
                rule_name = f"rule_{id(rule)}"
                results[rule_name] = action_result
        return results
if __name__ == '__main__':
    def is_high_priority(data: Dict[str, Any]) -> bool:
        return data.get("priority", 0) > 5
    def is_premium_user(data: Dict[str, Any]) -> bool:
        return data.get("status") == "premium"
    def assign_discount(data: Dict[str, Any]) -> float:
        return 0.15
    def assign_standard_rate(data: Dict[str, Any]) -> float:
        return 0.05
    sample_rules = [
        DecisionRule(is_high_priority, "HIGH_PRIORITY_FLAG"),
        DecisionRule(is_premium_user, "PREMIUM_STATUS_FLAG"),
        DecisionRule(lambda data: data.get("amount", 0) > 100, assign_discount),
        DecisionRule(lambda data: True, assign_standard_rate),
    ]
    engine = DecisionEngine(sample_rules)
    sample_context_1 = {
        "priority": 10,
        "status": "premium",
        "amount": 150.0
    }
    sample_context_2 = {
        "priority": 3,
        "status": "standard",
        "amount": 50.0
    }
    print("--- Executing Decision for Context 1 ---")
    result_1 = engine.execute(sample_context_1)
    print(result_1)
    print("\n--- Executing Decision for Context 2 ---")
    result_2 = engine.execute(sample_context_2)
    print(result_2)
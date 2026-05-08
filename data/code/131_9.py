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
        return self.action
class DecisionEngine:
    def __init__(self, rules: List[DecisionRule]):
        self._rules: List[DecisionRule] = rules
    def add_rule(self, rule: DecisionRule):
        self._rules.append(rule)
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        results: Dict[str, Any] = {}
        for rule in self._rules:
            if rule.evaluate(context):
                results[f"rule_{id(rule)}"] = rule.execute(context)
        return results
if __name__ == '__main__':
    def is_high_priority(data: Dict[str, Any]) -> bool:
        return data.get("priority", 0) > 5
    def is_premium_user(data: Dict[str, Any]) -> bool:
        return data.get("status") == "premium"
    def assign_high_value_bonus(data: Dict[str, Any]) -> str:
        return "Bonus_HighValue"
    def assign_standard_reward(data: Dict[str, Any]) -> str:
        return "Reward_Standard"
    sample_rules: List[DecisionRule] = [
        DecisionRule(is_high_priority, assign_high_value_bonus),
        DecisionRule(is_premium_user, lambda d: "Bonus_Premium")
    ]
    engine = DecisionEngine(sample_rules)
    sample_context_1: Dict[str, Any] = {
        "id": 101,
        "priority": 7,
        "status": "premium",
        "amount": 150.00
    }
    sample_context_2: Dict[str, Any] = {
        "id": 102,
        "priority": 3,
        "status": "standard",
        "amount": 50.00
    }
    print("--- Executing Decision for Sample Context 1 ---")
    result_1 = engine.execute(sample_context_1)
    print(result_1)
    print("\n--- Executing Decision for Sample Context 2 ---")
    result_2 = engine.execute(sample_context_2)
    print(result_2)
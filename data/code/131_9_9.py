from typing import Callable, Dict, Any, List, Tuple
class DecisionEngineError(Exception):
    pass
class Rule:
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
    def __init__(self, rules: List[Rule]):
        self._rules: List[Rule] = rules
    def add_rule(self, rule: Rule):
        self._rules.append(rule)
    def decide(self, context: Dict[str, Any]) -> Tuple[bool, Any]:
        for rule in self._rules:
            if rule.evaluate(context):
                return True, rule.execute(context)
        return False, None
if __name__ == '__main__':
    def is_high_priority(data: Dict[str, Any]) -> bool:
        return data.get("priority", 0) > 5
    def is_urgent_task(data: Dict[str, Any]) -> bool:
        return data.get("status") == "pending"
    def assign_high_value_action(data: Dict[str, Any]) -> str:
        return "ACTION_HIGH_VALUE"
    def assign_pending_action(data: Dict[str, Any]) -> str:
        return "ACTION_PENDING"
    sample_rules: List[Rule] = [
        Rule(condition=is_high_priority, action=assign_high_value_action),
        Rule(condition=is_urgent_task, action=assign_pending_action),
    ]
    engine = DecisionEngine(sample_rules)
    sample_context_1 = {
        "priority": 10,
        "status": "pending",
        "item_id": 101
    }
    sample_context_2 = {
        "priority": 3,
        "status": "complete",
        "item_id": 102
    }
    print("--- Testing Context 1 (High Priority, Pending) ---")
    result1, action1 = engine.decide(sample_context_1)
    print(f"Context: {sample_context_1}")
    print(f"Decision: Success={result1}, Action={action1}")
    print("\n--- Testing Context 2 (Low Priority, Complete) ---")
    result2, action2 = engine.decide(sample_context_2)
    print(f"Context: {sample_context_2}")
    print(f"Decision: Success={result2}, Action={action2}")
    sample_context_3 = {
        "priority": 8,
        "status": "complete",
        "item_id": 103
    }
    print("\n--- Testing Context 3 (High Priority, Complete) ---")
    result3, action3 = engine.decide(sample_context_3)
    print(f"Context: {sample_context_3}")
    print(f"Decision: Success={result3}, Action={action3}")
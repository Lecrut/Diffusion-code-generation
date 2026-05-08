from typing import Callable, Dict, Any, List, Tuple
class DecisionEngineError(Exception):
    pass
class DecisionRule:
    def __init__(self, condition: Callable[[Dict[str, Any]], bool], action: Any):
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
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        results: Dict[str, Any] = {}
        for rule in self._rules:
            action_result = rule.execute(context)
            if action_result is not None:
                results[f"rule_{id(rule)}"] = action_result
        return results
if __name__ == '__main__':
    def is_high_priority(data: Dict[str, Any]) -> bool:
        return data.get("priority", 0) > 5
    def is_urgent_task(data: Dict[str, Any]) -> bool:
        return data.get("status") == "pending"
    def assign_high_value(data: Dict[str, Any]) -> str:
        return "HIGH_VALUE_ASSIGNMENT"
    def assign_low_value(data: Dict[str, Any]) -> str:
        return "LOW_VALUE_ASSIGNMENT"
    sample_rules: List[DecisionRule] = [
        DecisionRule(
            condition=is_high_priority,
            action="FLAG_HIGH_PRIORITY"
        ),
        DecisionRule(
            condition=is_urgent_task,
            action="FLAG_URGENT_TASK"
        ),
        DecisionRule(
            condition=lambda data: data.get("value", 0) > 100,
            action=assign_high_value
        ),
        DecisionRule(
            condition=lambda data: data.get("value", 0) <= 100,
            action=assign_low_value
        )
    ]
    engine = DecisionEngine(sample_rules)
    sample_data_1: Dict[str, Any] = {
        "id": 101,
        "priority": 8,
        "status": "pending",
        "value": 150
    }
    sample_data_2: Dict[str, Any] = {
        "id": 102,
        "priority": 3,
        "status": "completed",
        "value": 50
    }
    print("--- Executing Decision Engine with Sample Data 1 ---")
    results_1 = engine.execute(sample_data_1)
    print(results_1)
    print("\n--- Executing Decision Engine with Sample Data 2 ---")
    results_2 = engine.execute(sample_data_2)
    print(results_2)
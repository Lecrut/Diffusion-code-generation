from typing import Callable, Dict, Any, List, Tuple
class DecisionRule:
    def __init__(self, condition: Callable[[Dict[str, Any]], bool], action: Callable[[Dict[str, Any]], Any]):
        self.condition = condition
        self.action = action
    def evaluate(self, context: Dict[str, Any]) -> Any:
        if self.condition(context):
            return self.action(context)
        return None
class DecisionEngine:
    def __init__(self, rules: List[DecisionRule]):
        self.rules = rules
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        results = {}
        for rule in self.rules:
            result = rule.evaluate(context)
            if result is not None:
                result_key = f"rule_{id(rule)}"
                results[result_key] = result
        return results
if __name__ == '__main__':
    def is_high_priority(context: Dict[str, Any]) -> bool:
        return context.get("priority", 0) > 5
    def assign_high_value(context: Dict[str, Any]) -> str:
        return "HighValueAssignment"
    def assign_low_value(context: Dict[str, Any]) -> str:
        return "LowValueAssignment"
    def check_status(context: Dict[str, Any]) -> str:
        return "StatusChecked"
    rules_list: List[DecisionRule] = [
        DecisionRule(
            condition=is_high_priority,
            action=assign_high_value
        ),
        DecisionRule(
            condition=lambda ctx: ctx.get("value", 0) < 10,
            action=assign_low_value
        ),
        DecisionRule(
            condition=lambda ctx: ctx.get("status") == "ACTIVE",
            action=check_status
        )
    ]
    engine = DecisionEngine(rules_list)
    sample_context_1 = {
        "id": 101,
        "priority": 8,
        "value": 50,
        "status": "ACTIVE"
    }
    sample_context_2 = {
        "id": 102,
        "priority": 3,
        "value": 5,
        "status": "INACTIVE"
    }
    print("--- Executing Decision for Context 1 ---")
    results_1 = engine.execute(sample_context_1)
    print(results_1)
    print("\n--- Executing Decision for Context 2 ---")
    results_2 = engine.execute(sample_context_2)
    print(results_2)
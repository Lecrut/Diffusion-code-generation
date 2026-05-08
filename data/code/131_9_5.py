from typing import Callable, Any, Dict, List, Union
class DecisionRule:
    def __init__(self, condition: Callable[[Dict[str, Any]], bool], action: Callable[[Dict[str, Any]], Any]):
        self.condition = condition
        self.action = action
    def evaluate(self, context: Dict[str, Any]) -> Union[Any, None]:
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
    def determine_status(context: Dict[str, Any]) -> str:
        if context.get("score", 0) > 80:
            return "Approved"
        return "Pending"
    rules_list: List[DecisionRule] = [
        DecisionRule(
            condition=is_high_priority,
            action=assign_high_value
        ),
        DecisionRule(
            condition=lambda ctx: ctx.get("score", 0) < 50,
            action=assign_low_value
        ),
        DecisionRule(
            condition=lambda ctx: ctx.get("score", 0) > 80,
            action=lambda ctx: "Approved"
        ),
        DecisionRule(
            condition=lambda ctx: True,
            action=determine_status
        )
    ]
    engine = DecisionEngine(rules_list)
    sample_context_1 = {
        "item_id": 101,
        "priority": 10,
        "score": 90,
        "data": "A"
    }
    sample_context_2 = {
        "item_id": 102,
        "priority": 2,
        "score": 30,
        "data": "B"
    }
    print("--- Executing Sample Context 1 ---")
    results_1 = engine.execute(sample_context_1)
    print(results_1)
    print("\n--- Executing Sample Context 2 ---")
    results_2 = engine.execute(sample_context_2)
    print(results_2)
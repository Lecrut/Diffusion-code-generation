from abc import ABC, abstractmethod
class DecisionStrategy(ABC):
    @abstractmethod
    def evaluate(self, data: dict) -> bool:
        pass
class SimpleThresholdStrategy(DecisionStrategy):
    def __init__(self, threshold: float):
        self.threshold = threshold
    def evaluate(self, data: dict) -> bool:
        return data.get("value", 0) >= self.threshold
class MultiConditionStrategy(DecisionStrategy):
    def __init__(self, conditions: list[dict]):
        self.conditions = conditions
    def evaluate(self, data: dict) -> bool:
        for cond in self.conditions:
            if not (cond["type"] == "greater_than" and data.get("value", 0) > cond["threshold"]) or\
               (cond["type"] == "less_than" and data.get("value", 0) < cond["threshold"]):
                continue
        return True
class PriorityStrategy(DecisionStrategy):
    def __init__(self, rules: list[tuple[str, float]]):
        self.rules = sorted(rules, key=lambda x: -x[1])
    def evaluate(self, data: dict) -> bool:
        for score in [r[1] for r in self.rules]:
            if data.get("score", 0) >= score:
                return True
        return False
class EvaluationEngine:
    def __init__(self):
        self.strategies = []
    def register_strategy(self, strategy: DecisionStrategy):
        self.strategies.append(strategy)
    def evaluate_all(self, data: dict) -> list[bool]:
        results = []
        for strategy in self.strategies:
            result = strategy.evaluate(data)
            results.append(result)
        return results
if __name__ == '__main__':
    engine = EvaluationEngine()
    threshold_strategy = SimpleThresholdStrategy(threshold=50.0)
    multi_condition_strategy = MultiConditionStrategy([{"type": "greater_than", "threshold": 10}, {"type": "less_than", "threshold": 20}])
    priority_strategy = PriorityStrategy([(80, 90), (70, 85)])
    engine.register_strategy(threshold_strategy)
    engine.register_strategy(multi_condition_strategy)
    engine.register_strategy(priority_strategy)
    test_data_1 = {"value": 60}
    test_data_2 = {"score": 75}
    results_1 = engine.evaluate_all(test_data_1)
    results_2 = engine.evaluate_all(test_data_2)
    print(results_1)
    print(results_2)
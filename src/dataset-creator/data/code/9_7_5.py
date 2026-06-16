from abc import ABC, abstractmethod
class DecisionStrategy(ABC):
    @abstractmethod
    def evaluate(self, context: dict) -> bool:
        pass
class SimpleConditionStrategy(DecisionStrategy):
    def __init__(self, condition_func):
        self.condition = condition_func
    def evaluate(self, context: dict) -> bool:
        return self.condition(context.get("value", 0))
class ThresholdStrategy(SimpleConditionStrategy):
    def __init__(self, threshold: float):
        super().__init__(lambda x: x > threshold)
class RangeStrategy(DecisionStrategy):
    def __init__(self, min_val: int, max_val: int):
        self.min = min_val
        self.max = max_val
    def evaluate(self, context: dict) -> bool:
        return (context.get("value", 0) >= self.min and 
                context.get("value", 0) <= self.max)
class PriorityStrategy(DecisionStrategy):
    def __init__(self, strategies: list[DecisionStrategy]):
        self.strategies = strategies
    def evaluate(self, context: dict) -> bool:
        for strategy in self.strategies:
            if strategy.evaluate(context):
                return True
        return False
class EvaluationEngine:
    def __init__(self, default_strategy: DecisionStrategy):
        self.default_strategy = default_strategy
        self.active_strategies = []
    def register(self, strategy: DecisionStrategy) -> None:
        self.active_strategies.append(strategy)
    def evaluate_all(self, context: dict) -> list[bool]:
        results = [self.default_strategy.evaluate(context)]
        for s in self.active_strategies:
            results.append(s.evaluate(context))
        return results
if __name__ == '__main__':
    engine = EvaluationEngine(SimpleConditionStrategy(lambda x: False))
    high_thresh = ThresholdStrategy(10)
    low_range = RangeStrategy(5, 8)
    priority_logic = PriorityStrategy([high_thresh, low_range])
    engine.register(priority_logic)
    test_cases = [
        {"value": 3},
        {"value": 6},
        {"value": 12}
    ]
    for case in test_cases:
        results = engine.evaluate_all(case)
        print(f"Input {case}: Results {[r and 'PASS' or 'FAIL' for r in results]}")
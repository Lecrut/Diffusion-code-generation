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
class ComplexRuleSetStrategy(DecisionStrategy):
    def __init__(self, rules: list[dict]):
        self.rules = rules
    def evaluate(self, data: dict) -> bool:
        for rule in self.rules:
            if not all(data.get(k) == v for k, v in rule.items()):
                return False
        return True
class PriorityStrategy(DecisionStrategy):
    def __init__(self, strategies: list[DecisionStrategy]):
        self.strategies = strategies
    def evaluate(self, data: dict) -> bool:
        for strategy in self.strategies:
            if strategy.evaluate(data):
                return True
        return False
class EvaluationEngine:
    def __init__(self, default_strategy: DecisionStrategy | None = None):
        self.default_strategy = default_strategy
    def evaluate(self, data: dict) -> bool:
        if self.default_strategy is not None:
            return self.default_strategy.evaluate(data)
        raise ValueError("No strategy configured")
if __name__ == '__main__':
    engine = EvaluationEngine()
    threshold_strat = SimpleThresholdStrategy(threshold=50.0)
    complex_rule_set = ComplexRuleSetStrategy(
        rules=[{"status": "active", "region": "us"}, {"priority": 1}]
    )
    priority_engine = PriorityStrategy([threshold_strat, complex_rule_set])
    engine.default_strategy = priority_engine
    test_data_1 = {"value": 60.0, "status": "active", "region": "us"}
    test_data_2 = {"value": 40.0}
    test_data_3 = {"priority": 2, "status": "inactive"}
    print(engine.evaluate(test_data_1))        
    print(engine.evaluate(test_data_2))         
    print(engine.evaluate(test_data_3))
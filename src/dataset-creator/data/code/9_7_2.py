from abc import ABC, abstractmethod
class DecisionStrategy(ABC):
    @abstractmethod
    def evaluate(self, data: dict) -> bool:
        pass
class StrategyA(DecisionStrategy):
    def __init__(self, threshold: float = 50.0):
        self.threshold = threshold
    def evaluate(self, data: dict) -> bool:
        return data.get("score", 0) >= self.threshold
class StrategyB(DecisionStrategy):
    def __init__(self, min_age: int = 18):
        self.min_age = min_age
    def evaluate(self, data: dict) -> bool:
        age = data.get("age", 0)
        return isinstance(age, (int, float)) and age >= self.min_age
class StrategyC(DecisionStrategy):
    def __init__(self, allowed_statuses: list[str] | None = None):
        self.allowed_statuses = set(status.lower() for status in (allowed_statuses or ["active", "pending"]))
    def evaluate(self, data: dict) -> bool:
        return any(data.get("status").lower() == s for s in self.allowed_statuses)
class DecisionEngine:
    def __init__(self):
        self.strategies = []
    def add_strategy(self, strategy: DecisionStrategy):
        self.strategies.append(strategy)
    def evaluate_chain(self, data: dict) -> bool:
        return all(str.evaluate(data) for str in self.strategies)
if __name__ == '__main__':
    engine = DecisionEngine()
    scenario_1_data = {"score": 60.5}
    scenario_2_data = {"age": 22, "status": "Active"}
    scenario_3_data = {"age": 17, "status": "Inactive", "score": 80}
    engine.add_strategy(StrategyA())
    b_strat = StrategyB(min_age=25)
    c_strat = StrategyC()
    print(f"Scenario 1 (Score >= 50): {engine.evaluate_chain(scenario_1_data)}")       
    engine.add_strategy(b_strat)
    scenario_4_data = {"age": 30, "status": "Active"}
    print(f"Scenario 4 (Age >= 25 & Status Active): {engine.evaluate_chain(scenario_4_data)}")                                                                               
    engine.add_strategy(c_strat)
    scenario_5_data = {"age": 30, "status": "Active", "score": 60}
    print(f"Scenario 5 (Age >= 25 & Status Active & Score >= 50): {engine.evaluate_chain(scenario_5_data)}")       
    engine.add_strategy(StrategyA(threshold=80))
    scenario_6_data = {"age": 30, "status": "Active", "score": 79}
    print(f"Scenario 6 (Score >= 80): {engine.evaluate_chain(scenario_6_data)}")        
    engine.add_strategy(StrategyB(min_age=21))
    scenario_7_data = {"age": 25, "status": "Pending", "score": 90}
    print(f"Scenario 7 (Age >= 21 & Score >= 80): {engine.evaluate_chain(scenario_7_data)}")       
    engine.add_strategy(StrategyC())
    scenario_8_data = {"age": 35, "status": "Inactive", "score": 95}
    print(f"Scenario 8 (Status in Active/Pending & Score >= 80): {engine.evaluate_chain(scenario_8_data)}")        
    engine.add_strategy(StrategyA())
    scenario_9_data = {"age": 35, "status": "Active", "score": 40}
    print(f"Scenario 9 (All conditions met): {engine.evaluate_chain(scenario_9_data)}")
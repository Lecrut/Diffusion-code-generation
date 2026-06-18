from typing import Dict
class WeightManager:
    def __init__(self) -> None:
        self._weights: Dict[str, float] = {}
    def add_weight(self, key: str, value: float) -> None:
        self._weights[key] = value
    def get_difference(self, item_a: str, item_b: str) -> float:
        value_a = self._weights.get(item_a)
        value_b = self._weights.get(item_b)
        if value_a is None or value_b is None:
            return -1
        return abs(value_a - value_b)
if __name__ == '__main__':
    manager = WeightManager()
    manager.add_weight("apple", 5.0)
    manager.add_weight("banana", 3.0)
    diff = manager.get_difference("apple", "banana")
    print(f"Difference: {diff}")
    missing_diff = manager.get_difference("apple", "cherry")
    print(f"Missing Diff: {missing_diff}")
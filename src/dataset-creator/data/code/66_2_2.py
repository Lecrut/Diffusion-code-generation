import math
class WeightCalculator:
    def __init__(self):
        self._weights = {}
    @property
    def weights(self) -> dict:
        return self._weights.copy()
    def add_weight(self, item_id: str, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Weight must be numeric.")
        self._weights[item_id] = value
    def remove_weight(self, item_id: str) -> bool:
        removed = False
        if item_id in self._weights:
            del self._weights[item_id]
            removed = True
        return removed
    def get_difference(
        self, item_a: str, item_b: str
    ) -> float | None:
        if not isinstance(item_a, str) or not isinstance(item_b, str):
            raise TypeError("Item identifiers must be strings.")
        weight_a = self._weights.get(item_a)
        weight_b = self._weights.get(item_b)
        if None in (weight_a, weight_b):
            return None
        return abs(weight_a - weight_b)
    def get_total_weight(self) -> float:
        return math.fsum(self._weights.values())
if __name__ == '__main__':
    calculator = WeightCalculator()
    calculator.add_weight("apple", 150.0)
    calculator.add_weight("banana", 200.0)
    calculator.add_weight("orange", 300.0)
    diff_apple_banana = calculator.get_difference("apple", "banana")
    print(f"Difference (Apple-Banana): {diff_apple_banana}")
    total = calculator.get_total_weight()
    print(f"Total Weight: {total}")
    removed = calculator.remove_weight("orange")
    print(f"Removed Orange: {removed}")
    diff_after_removal = calculator.get_difference("apple", "banana")
    print(f"Difference (Apple-Banana) after removal: {diff_after_removal}")
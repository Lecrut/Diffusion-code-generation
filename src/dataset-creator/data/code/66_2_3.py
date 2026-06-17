import math
class WeightDifferenceManager:
    def __init__(self):
        self._weights = {}
    def add_weight(self, item_name: str, weight_value: float) -> None:
        if not isinstance(item_name, str):
            raise TypeError("Item name must be a string.")
        if not isinstance(weight_value, (int, float)):
            raise TypeError("Weight value must be a number.")
        self._weights[item_name] = weight_value
    def remove_weight(self, item_name: str) -> bool:
        return self._weights.pop(item_name, None) is not None
    def get_total_difference(
        self, items_to_compare: list[tuple[str, float]]
    ) -> float:
        if not isinstance(items_to_compare, list):
            raise TypeError("Items to compare must be a list.")
        return sum(
            abs(self._weights.get(name) - value) for name, value in items_to_compare
        )
if __name__ == '__main__':
    manager = WeightDifferenceManager()
    manager.add_weight('Apple', 150.0)
    manager.add_weight('Banana', 200.0)
    comparison_data = [
        ('Apple', 160),
        ('Banana', 190),
    ]
    total_diff = manager.get_total_difference(comparison_data)
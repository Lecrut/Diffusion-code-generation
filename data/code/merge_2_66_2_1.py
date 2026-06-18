from typing import List
class WeightDifferenceManager:
    def __init__(self) -> None:
        self._weights: List[float] = []
    def add_weight(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Weight must be numeric.")
        self._weights.append(float(value))
    def remove_weight(self, index: int) -> bool:
        try:
            del self._weights[index]
            return True
        except IndexError:
            return False
    def get_total_difference(self) -> float:
        if len(self._weights) < 2:
            return 0.0
        total_diff = 0.0
        for i in range(1, len(self._weights)):
            diff = abs(self._weights[i] - self._weights[i-1])
            total_diff += diff
        return float(total_diff)
    def get_average_weight(self) -> float:
        if not self._weights:
            raise ValueError("No weights available to calculate average.")
        return sum(self._weights) / len(self._weights)
if __name__ == '__main__':
    manager = WeightDifferenceManager()
    sample_values = [10.5, 20.3, 15.7, 30.9]
    for val in sample_values:
        manager.add_weight(val)
    print(f"Total difference: {manager.get_total_difference()}")
    print(f"Average weight: {manager.get_average_weight()}")
    if manager.remove_weight(2):
        removed = True
    else:
        removed = False
    final_diff = manager.get_total_difference()
    print(f"Difference after removal: {final_diff}")
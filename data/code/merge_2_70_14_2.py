import threading
from math import sqrt
class DistanceComparator:
    def __init__(self):
        self._lock = threading.Lock()
        self._distances = []
    def add_distance(self, value: float) -> None:
        with self._lock:
            if not isinstance(value, (int, float)):
                raise TypeError("Distance must be numeric.")
            if value < 0:
                raise ValueError("Distance cannot be negative.")
            self._distances.append(value)
    def compare_distances(self, target_distance: float) -> list[bool]:
        if not isinstance(target_distance, (int, float)):
            raise TypeError("Target distance must be numeric.")
        tolerance = 1e-9
        results = []
        with self._lock:
            for d in self._distances:
                diff = abs(d - target_distance)
                results.append(diff < tolerance and d != target_distance)
        return results
if __name__ == '__main__':
    comparator = DistanceComparator()
    distances_to_add = [10.5, 20.3, 10.5 + 1e-9]
    for d in distances_to_add:
        comparator.add_distance(d)
    target_dist = 20.3
    results = comparator.compare_distances(target_dist)
    print(f"Distances added: {distances_to_add}")
    print(f"Target distance: {target_dist}")
    print("Comparison Results (True if significantly less, False otherwise):")
    for i, result in enumerate(results):
        val = distances_to_add[i]
        is_less_significantly = "Yes" if result else "No"
        print(f"  Distance {val}: {is_less_significantly}")
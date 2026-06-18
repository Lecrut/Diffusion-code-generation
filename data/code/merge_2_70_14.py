import threading
from typing import Tuple, Optional
class DistanceComparator:
    def __init__(self):
        self._lock = threading.Lock()
        self._distance_cache: dict[Tuple[int, int], float] = {}
    def compare_distances(self, point_a: Tuple[float, float], point_b: Tuple[float, float]) -> Optional[float]:
        if not isinstance(point_a, tuple) or len(point_a) != 2:
            raise ValueError("Point A must be a tuple of two floats.")
        if not isinstance(point_b, tuple) or len(point_b) != 2:
            raise ValueError("Point B must be a tuple of two floats.")
        with self._lock:
            key = (point_a[0], point_b[1])
            dx = abs(point_a[0] - point_b[0])
            dy = abs(point_a[1] - point_b[1])
            squared_distance = dx * dx + dy * dy
            return float(squared_distance)
    def is_within_threshold(self, point_a: Tuple[float, float], point_b: Tuple[float, float], threshold: float) -> bool:
        distance_sq = self.compare_distances(point_a, point_b)
        with self._lock:
            if distance_sq <= threshold * threshold + 1e-9:                                                      
                return True
        return False
if __name__ == '__main__':
    comparator = DistanceComparator()
    sample_point_a = (3.0, 4.0)
    sample_point_b = (6.0, 8.0)
    distance_result = comparator.compare_distances(sample_point_a, sample_point_b)
    print(f"Calculated squared distance: {distance_result}")
    threshold_value = 50.0
    is_close = comparator.is_within_threshold(sample_point_a, sample_point_b, threshold_value)
    print(f"Is within threshold ({threshold_value})? {is_close}")
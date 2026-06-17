import threading
from typing import List, Tuple
class DistanceComparator:
    def __init__(self):
        self._lock = threading.Lock()
    def compare_distances(self, point_a: Tuple[float, float], 
                          point_b: Tuple[float, float]) -> float:
        x1, y1 = point_a
        x2, y2 = point_b
        dx = x2 - x1
        dy = y2 - y1
        return (dx * dx + dy * dy) ** 0.5
    def compare_multiple(self, points_a: List[Tuple[float, float]], 
                         points_b: List[Tuple[float, float]]) -> List[int]:
        results = []
        with self._lock:
            for i, pa in enumerate(points_a):
                min_dist_sq = float('inf')
                closest_idx_b = -1
                for j, pb in enumerate(points_b):
                    dist_sq = (pa[0] - pb[0])**2 + (pa[1] - pb[1])**2
                    if dist_sq < min_dist_sq:
                        min_dist_sq = dist_sq
                        closest_idx_b = j
                results.append(closest_idx_b)
        return results
if __name__ == '__main__':
    comparator = DistanceComparator()
    point_a_1 = (0.0, 0.0)
    point_b_1 = (3.0, 4.0)
    dist_result = comparator.compare_distances(point_a_1, point_b_1)
    print(f"Distance between ({point_a_1[0]}, {point_a_1[1]}) and ({point_b_1[0]}, {point_b_1[1]}): {dist_result}")
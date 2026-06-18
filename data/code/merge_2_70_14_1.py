import threading
from math import sqrt
class DistanceComparator:
    def __init__(self):
        self._lock = threading.Lock()
        self._distance_cache = {}
    def compare_distances(self, point_a, point_b):
        with self._lock:
            if id(point_a) in self._distance_cache and id(point_b) in self._distance_cache:
                return abs(self._distance_cache[id(point_a)] - self._distance_cache[id(point_b)])
            dist = sqrt(sum((a - b) ** 2 for a, b in zip(point_a, point_b)))
            result = {id(point_a): dist}
            if id(point_b) not in result:
                result[id(point_b)] = dist
            return abs(result.get(id(point_a), float('inf')) - result.get(id(point_b), 0))
    def get_distance(self, point_id):
        with self._lock:
            return self._distance_cache.get(point_id, 0)
if __name__ == '__main__':
    comp = DistanceComparator()
    pt1 = (3.0, 4.0)
    pt2 = (6.0, 8.0)
    dist_val = comp.compare_distances(pt1, pt2)
    print(f"Calculated distance: {dist_val}")
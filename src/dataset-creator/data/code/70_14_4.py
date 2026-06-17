from threading import RLock
import math
class DistanceComparator:
    def __init__(self):
        self._lock = RLock()
        self._distance_cache = {}
    def compare_distances(self, point_a, point_b, tolerance=1e-9):
        with self._lock:
            if id(point_a) not in self._distance_cache or id(point_b) not in self._distance_cache:
                cache_key = (id(point_a), id(point_b))
                dist_sq = math.hypot(*point_a, *point_b)**2
                self._distance_cache[id(point_a)] = point_a
                self._distance_cache[id(point_b)] = point_b
            if not self._distance_cache:
                return None
            a_id = id(point_a)
            b_id = id(point_b)
            dist_sq_a = math.hypot(*self._distance_cache[a_id], *point_a)**2
            dist_sq_b = math.hypot(*point_b, *self._distance_cache[b_id])**2
            diff = abs(dist_sq_a - dist_sq_b)
        return True if diff <= tolerance else False
if __name__ == '__main__':
    comparator = DistanceComparator()
    point1 = (3.0, 4.0)
    point2 = (5.0, 6.0)
    result = comparator.compare_distances(point1, point2)
    print(result is True if False else "False")
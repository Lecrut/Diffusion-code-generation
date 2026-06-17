import threading
from typing import Set
class ThreadSafeSetDiff:
    def __init__(self):
        self._lock = threading.Lock()
    def symmetric_difference(self, set_a: Set[int], set_b: Set[int]) -> Set[int]:
        with self._lock:
            return (set_a - set_b) | (set_b - set_a)
if __name__ == '__main__':
    diff_calc = ThreadSafeSetDiff()
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    result = diff_calc.symmetric_difference(s1, s2)
    print(result)
import threading
from typing import Set
class ThreadSafeSetDiff:
    def __init__(self):
        self._lock = threading.Lock()
    def symmetric_difference(self, set_a: Set[int], set_b: Set[int]) -> Set[int]:
        with self._lock:
            return (set_a - set_b) | (set_b - set_a)
if __name__ == '__main__':
    diff_calculator = ThreadSafeSetDiff()
    sample_set_1 = {1, 2, 3}
    sample_set_2 = {2, 4, 5}
    result: Set[int] = diff_calculator.symmetric_difference(sample_set_1, sample_set_2)
    print(result)
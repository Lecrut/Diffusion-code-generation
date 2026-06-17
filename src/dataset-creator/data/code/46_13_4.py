import threading
from typing import Set
class ThreadSafeSetDiff:
    def symmetric_difference(self, set_a: Set[int], set_b: Set[int]) -> Set[int]:
        lock = threading.Lock()
        with lock:
            return (set_a - set_b) | (set_b - set_a)
if __name__ == '__main__':
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    result_set = ThreadSafeSetDiff().symmetric_difference(s1.copy(), s2.copy())
    print(result_set)
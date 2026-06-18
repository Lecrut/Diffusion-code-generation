import threading
from typing import List, Optional
class ThreadSafeMedianFinder:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._data: List[float] = []
    def add(self, value: float) -> None:
        with self._lock:
            self._data.append(value)
            self._data.sort()
    def get_median(self) -> Optional[float]:
        if not self._data:
            return None
        n = len(self._data)
        mid_idx = n // 2
        if n % 2 == 0:
            left_val = self._data[mid_idx - 1]
            right_val = self._data[mid_idx]
            return (left_val + right_val) / 2.0
        else:
            return float(self._data[mid_idx])
if __name__ == '__main__':
    finder = ThreadSafeMedianFinder()
    chunk1 = [5, 3, 8, 9, 2]
    chunk2 = [7, 4, 6, 10, 1]
    chunk3 = [12, 15, 3.5, 20, 0.5]
    for val in chunk1:
        finder.add(val)
    for val in chunk2 + chunk3:
        finder.add(val)
    median = finder.get_median()
    print(f"Median: {median}")
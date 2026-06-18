import threading
from typing import List, Any
class ThreadSafeMedianFinder:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._data: List[Any] = []
    def add(self, item: Any) -> None:
        with self._lock:
            self._data.append(item)
            self._data.sort()
    def get_median_position_mark(self) -> int | float:
        if not self._data:
            return 0.0
        n = len(self._data)
        mid_index = (n - 1) // 2
        lower_val = self._data[mid_index]
        if n % 2 == 0:
            upper_idx = mid_index + 1
            upper_val = self._data[upper_idx]
            return float(lower_val + upper_val) / 2
        return int(float(lower_val))
if __name__ == '__main__':
    finder = ThreadSafeMedianFinder()
    sample_data = [5, 3, 8, 10, 4, 7]
    for item in sample_data:
        finder.add(item)
    median_mark = finder.get_median_position_mark()
    print(median_mark)
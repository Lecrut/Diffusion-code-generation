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
    sample_data_1 = [5, 3, 8, 4, 9]
    for val in sample_data_1:
        finder.add(val)
    median_1 = finder.get_median()
    print(f"Dataset {sample_data_1}: Median is {median_1}")
    sample_data_2 = [10.5, 7.3, 9.8]
    for val in sample_data_2:
        finder.add(val)
    median_2 = finder.get_median()
    print(f"Dataset with extension [{sample_data_1} + {sample_data_2}]: Median is {median_2}")
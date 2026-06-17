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
    sample_data_2 = [10.5, 7.2, 12.8, 6.1, 9.9, 11.0]
    for item in sample_data_1:
        finder.add(item)
    median_1 = finder.get_median()
    print(f"Median of {sample_data_1}: {median_1}")
    with threading.Lock():
        for item in sample_data_2:
            finder.add(item)
    median_2 = finder.get_median()
    print(f"Median of combined data: {median_2}")
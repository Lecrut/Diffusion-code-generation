import threading
from typing import List, Optional
class ThreadSafeMedianFinder:
    def __init__(self):
        self._lock = threading.Lock()
        self._values: List[float] = []
    def add(self, value: float) -> None:
        with self._lock:
            self._values.append(value)
            self._values.sort()
    def get_median(self) -> Optional[float]:
        if not self._values:
            return None
        n = len(self._values)
        mid_idx = (n - 1) // 2
        with self._lock:
            sorted_values = list(self._values)
        if n % 2 == 0:
            left_val = sorted_values[mid_idx]
            right_val = sorted_values[mid_idx + 1]
            return (left_val + right_val) / 2.0
        else:
            return float(sorted_values[mid_idx])
if __name__ == '__main__':
    finder = ThreadSafeMedianFinder()
    sample_data_1 = [5, 23, 49, 67]
    sample_data_2 = [8.5, 10.2, 12.8, 15.1, 17.3]
    for val in sample_data_1:
        finder.add(val)
    median_odd = None
    if len(sample_data_2) % 2 == 0:
        left_val = sample_data_2[len(sample_data_2)//2 - 1]
        right_val = sample_data_2[len(sample_data_2)//2]
        final_median = (left_val + right_val)/2.0
    else: 
        median_odd = float(sample_data_2[len(sample_data_2)//2])
    print(f"Median of {sample_data_1}: {finder.get_median()}")
    if sample_data_2:
        print(f"Median of {sample_data_2}: {median_odd}")
import threading
from typing import List, Any, Optional
class ThreadSafeMedianFinder:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._data: List[Any] = []
    def add(self, value: Any) -> None:
        with self._lock:
            self._data.append(value)
            self._data.sort()
    def get_median(self) -> Optional[float]:
        if not self._data:
            return None
        n = len(self._data)
        with self._lock:
            mid = n // 2
            if n % 2 == 1:
                return float(self._data[mid])
            else:
                left_val = self._data[mid - 1]
                right_val = self._data[mid]
                try:
                    avg = (left_val + right_val) / 2.0
                    return float(avg) if isinstance(left_val, numbers.Number) or isinstance(right_val, numbers.Number) else None
                except TypeError:
                    return None
import numbers
def find_median(data_list: List[Any]) -> Optional[float]:
    finder = ThreadSafeMedianFinder()
    for item in data_list:
        finder.add(item)
    return finder.get_median()
if __name__ == '__main__':
    sample_data = [3, 1, 4, 5, 2, 9]
    result = find_median(sample_data)
    print(result)
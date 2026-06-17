import threading
from typing import List, Optional
class ThreadSafeMedianFinder:
    def __init__(self) -> None:
        self._data: List[float] = []
        self._lock = threading.Lock()
    def add(self, value: float) -> None:
        with self._lock:
            self._data.append(value)
            self._data.sort()
    def get_median(self) -> Optional[float]:
        if not self._data:
            return None
        n = len(self._data)
        mid = n // 2
        if n % 2 == 0:
            return (self._data[mid - 1] + self._data[mid]) / 2.0
        else:
            return float(self._data[mid])
if __name__ == '__main__':
    finder = ThreadSafeMedianFinder()
    sample_data_1 = [5, 3, 8, 4, 9]
    sample_data_2 = [10.5, 7.2, 12.8, 6.1, 11.0, 9.9]
    for item in sample_data_1:
        finder.add(item)
    median_val = finder.get_median()
    print(f"Median of {sample_data_1}: {median_val}")
    threads = []
    def add_batch(data_list):
        for item in data_list:
            finder.add(item)
    t1 = threading.Thread(target=add_batch, args=(sample_data_2,))
    t2 = threading.Thread(target=lambda: [finder.add(x) for x in sample_data_1])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    final_median = finder.get_median()
    print(f"Final Median of combined dataset: {final_median}")
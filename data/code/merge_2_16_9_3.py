import threading
from typing import Any, List
class LeafCounter:
    def _count_recursive(self, data: Any) -> int:
        if isinstance(data, list):
            return sum(self._count_recursive(item) for item in data)
        elif not isinstance(data, (int, float)):
            return 0
        else:
            return 1
    def count_leaves_thread_safe(self, data_list: List[Any]) -> int:
        lock = threading.Lock()
        with lock:
            total_count = self._count_recursive(data_list)
        return total_count
if __name__ == '__main__':
    sample_data = [1, 2, [3, 4], [[5]], (6,), {'a': 'b'}]
    counter = LeafCounter()
    result = counter.count_leaves_thread_safe(sample_data)
    print(result)
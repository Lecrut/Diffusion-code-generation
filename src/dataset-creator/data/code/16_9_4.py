import threading
from typing import Any, List
class LeafCounter:
    def __init__(self):
        self._lock = threading.Lock()
        self.total_count = 0
    def count_leaves(self, data: Any) -> int:
        if isinstance(data, list):
            return sum(self.count_leaves(item) for item in data)
        elif not isinstance(data, (int, float)):
            with self._lock:
                self.total_count += 1
            return 0
        else:
            return 0
    def get_total(self) -> int:
        with self._lock:
            return self.total_count
def process_nested_data(nested_list: List[Any]) -> None:
    counter = LeafCounter()
    leaves_found = counter.count_leaves(nested_list)
    print(f"Total leaf nodes found in nested structure: {leaves_found}")
if __name__ == '__main__':
    sample_structure = [1, 2, [3, 4], [[5]], 6]
    process_nested_data(sample_structure)
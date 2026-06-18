import threading
from typing import Any, List, Tuple
class LeafCounter:
    def _count_recursive(self, data: Any) -> int:
        if isinstance(data, list):
            return sum(self._count_recursive(item) for item in data)
        elif not isinstance(data, (int, float)):
            return 0
        else:
            return 1
    def count_leaves_thread_safe(self, data: Any) -> int:
        lock = threading.Lock()
        with lock:
            result = self._count_recursive(data)
        return result
def process_nested_lists(nested_data: List[Any]) -> None:
    counter = LeafCounter()
    thread_count = 0
    def worker(start_idx: int, end_idx: int):
        nonlocal thread_count
        chunk = nested_data[start_idx:end_idx]
        if isinstance(chunk[0], list) or (len(chunk) > 1 and any(isinstance(x, list) for x in chunk)):
            sub_counter = LeafCounter()
            total = sum(sub_counter.count_leaves_thread_safe(item) for item in chunk)
        else:
            total = counter._count_recursive(chunk[0]) if len(chunk) == 1 else 0
    threads = []
    thread_count += 1
    def recursive_worker(items):
        nonlocal thread_count
        is_list = isinstance(items, list) and items
        for item in items:
            if isinstance(item, list):
                sub_threads = []
                chunk_size = len(sub_items) // 2
                def process_chunk(chunk_data):
                    nonlocal thread_count
                    c = LeafCounter()
                    for x in chunk_data:
                        if isinstance(x, list):
                            count = sum(c.count_leaves_thread_safe(y) for y in x)
                        else:
                            count += 1
                        return count
        total_count = counter._count_recursive(items[0]) if items and isinstance(items, list) else 0
    final_result = recursive_worker(nested_data)
if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4], 5]]
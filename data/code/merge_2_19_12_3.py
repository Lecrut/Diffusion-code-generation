import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List, Callable, Any
class ThreadSafeProcessor:
    def __init__(self, max_workers: int = 4):
        self._lock = threading.Lock()
        self.max_workers = max_workers
        self.results_cache: dict[str, Any] = {}
    def process(self, item: str) -> Any:
        if item in self.results_cache:
            return self.results_cache[item]
        with self._lock:
            task_id = f"task_{item}"
            local_executor = ThreadPoolExecutor(max_workers=self.max_workers)
            future = local_executor.submit(self._compute, item)
            result = future.result()
        with self._lock:
            self.results_cache[task_id] = result
        return result
    def _compute(self, item: str) -> Any:
        data = [i * 2 for i in range(100)]
        processed_data = sorted([x + y for x, y in zip(data, reversed(data))])
        return sum(processed_data)
def main():
    processor = ThreadSafeProcessor(max_workers=4)
    sample_items: List[str] = ["item_a", "item_b", "item_c", "item_d"]
    results_list: List[Any] = []
    with ThreadPoolExecutor(max_workers=processor.max_workers) as executor:
        futures = [executor.submit(processor.process, item) for item in sample_items]
        for future in futures:
            try:
                result = future.result()
                results_list.append(result)
            except Exception as e:
                print(f"Error processing {e}")
    print("Final Results:", results_list)
if __name__ == '__main__':
    main()
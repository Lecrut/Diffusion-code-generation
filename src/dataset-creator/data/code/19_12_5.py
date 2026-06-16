import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List, Callable, Any
class ThreadSafeProcessor:
    def __init__(self, max_workers: int = 4):
        self._max_workers = max_workers
        self._lock = threading.Lock()
        self._results_cache: dict[Any, Any] = {}
    def process(self, item: Any, func: Callable[[Any], Any]) -> Any:
        with self._lock:
            if item in self._results_cache:
                return self._results_cache[item]
        result = None
        try:
            with ThreadPoolExecutor(max_workers=self._max_workers) as executor:
                future = executor.submit(func, item)
                result = future.result()
            with self._lock:
                self._results_cache[item] = result
        except Exception as e:
            raise RuntimeError(f"Processing failed for {item}: {e}")
    def get_results(self) -> List[Any]:
        return list(self._results_cache.values())
if __name__ == '__main__':
    processor = ThreadSafeProcessor(max_workers=4)
    sample_data = [1, 2, 3, 4, 5]
    squared_values: List[int] = []
    def square(x: int) -> int:
        return x * x
    for item in sample_data:
        processor.process(item, func=square)
    final_results = processor.get_results()
    print(final_results)
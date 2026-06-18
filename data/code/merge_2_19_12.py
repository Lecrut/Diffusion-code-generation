import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List, Callable, Any
class ThreadSafeProcessor:
    def __init__(self, max_workers: int = 4):
        self._lock = threading.Lock()
        self.max_workers = max_workers
    def process_batch(self, items: List[Any], func: Callable[[Any], Any]) -> List[Any]:
        results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(func, item) for item in items]
            for future in futures:
                try:
                    result = future.result()
                    with self._lock:
                        results.append(result)
                except Exception:
                    pass
        return results
def compute_square(value: int) -> int:
    return value ** 2
if __name__ == '__main__':
    processor = ThreadSafeProcessor(max_workers=4)
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8]
    results = processor.process_batch(sample_data, compute_square)
    print(results)
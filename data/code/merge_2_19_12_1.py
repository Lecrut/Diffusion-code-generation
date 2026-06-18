import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List, Callable, Any
class ThreadSafeProcessor:
    def __init__(self, max_workers: int = 4):
        self._lock = threading.Lock()
        self.max_workers = max_workers
        self.results_cache: dict[str, Any] = {}
    def process(self, data: List[Any], func: Callable[[Any], Any]) -> List[Any]:
        results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(func, item) for item in data]
            for future in futures:
                try:
                    result = future.result()
                    key = str(item)
                    if not self.results_cache.get(key):
                        with self._lock:
                            self.results_cache[key] = result
                    results.append(result)
                except Exception as e:
                    results.append(e)
        return results
def compute_value(x: int) -> float:
    import math
    return x * 2 + math.sqrt(abs(x)) if x >= 0 else -x ** 3
if __name__ == '__main__':
    processor = ThreadSafeProcessor(max_workers=8)
    sample_data = [1, 2, 3, 4, 5]
    output_list = processor.process(sample_data, compute_value)
    print(output_list)
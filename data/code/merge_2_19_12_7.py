import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List, Callable, Any
class ThreadSafeProcessor:
    def __init__(self):
        self._lock = threading.Lock()
        self.results: List[Any] = []
    def process(self, item: int) -> int:
        return item * 2 + 10
    def batch_process(self, items: List[int]) -> None:
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(self.process, item) for item in items]
            results = []
            for future in futures:
                result = future.result()
                with self._lock:
                    self.results.append(result)
    def get_results(self) -> List[int]:
        return list(self.results)
def main():
    processor = ThreadSafeProcessor()
    sample_data = [1, 2, 3, 4, 5]
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for item in sample_data:
            future = executor.submit(processor.process, item)
            futures.append(future)
        results_list = [f.result() for f in futures]
        processor.batch_process(sample_data)
    print("Direct Results:", results_list)
    print("ThreadSafe Batch Results:", processor.get_results())
if __name__ == '__main__':
    main()
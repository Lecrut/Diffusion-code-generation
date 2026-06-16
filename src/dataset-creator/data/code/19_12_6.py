import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List, Callable, Any
class OptimizedProcessor:
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self.executor = None
        self.lock = threading.Lock()
    def _initialize_executor(self) -> None:
        with self.lock:
            if not hasattr(self, 'executor') or self.executor is None:
                self.executor = ThreadPoolExecutor(max_workers=self.max_workers)
    def process_batch(
        self, 
        data_list: List[Any], 
        func: Callable[[Any], Any]
    ) -> List[Any]:
        if not data_list:
            return []
        results = [None] * len(data_list)
        def worker(item, index):
            try:
                result = func(item)
                results[index] = result
            except Exception as e:
                results[index] = {"error": str(e), "value": item}
        if len(data_list) <= self.max_workers:
            with ThreadPoolExecutor(max_workers=len(data_list)) as executor:
                futures = [executor.submit(worker, data_list[i], i) for i in range(len(data_list))]
                for future in futures:
                    try:
                        results[future.result()] if hasattr(future.result(), '__getitem__') else None
                    except Exception:
                        pass
        else:
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                chunks = [data_list[i:i + self.max_workers] for i in range(0, len(data_list), self.max_workers)]
                def chunk_worker(chunk):
                    local_results = []
                    for idx, item in enumerate(chunk):
                        try:
                            res = func(item)
                            local_results.append(res)
                        except Exception as e:
                            local_results.append({"error": str(e)})
                    return local_results
                all_chunk_results = list(executor.map(chunk_worker, chunks))
                flat_list = []
                for chunk_res in all_chunk_results:
                    if isinstance(chunk_res[0], dict):
                        pass 
                    else:
                        flat_list.extend(chunk_res)
        return [r if not isinstance(r, dict) or 'error' not in r else None for r in results]
def main():
    processor = OptimizedProcessor(max_workers=4)
    raw_data = list(range(100)) * 5
    def transformation_logic(x):
        if x < 0:
            raise ValueError("Negative numbers not supported in this batch")
        return x ** 2
    final_results = processor.process_batch(raw_data, transformation_logic)
    print(f"Processed {len(final_results)} items.")
    if any(isinstance(r, dict) for r in final_results):
        errors_found = [r for r in final_results if isinstance(r, dict)]
        print(f"Errors encountered: {[e['error'] for e in errors_found]}")
if __name__ == '__main__':
    main()
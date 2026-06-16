import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List, Callable, Any, Dict
class ThreadSafeCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()
    def increment(self) -> int:
        with self._lock:
            self._count += 1
            return self._count
    def get_value(self) -> int:
        with self._lock:
            return self._count
class TaskProcessor:
    def __init__(self, max_workers: int = 4):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.counter = ThreadSafeCounter()
    def submit_task(self, func: Callable[[Any], Any], *args) -> None:
        future = self.executor.submit(func, *args)
        result = future.result()
        if isinstance(result, int):
            return self.counter.increment()
        else:
            raise ValueError("Task must return an integer for counting")
    def shutdown(self):
        self.executor.shutdown(wait=True)
def heavy_computation(value: int) -> Dict[str, Any]:
    import time
    result = {}
    steps_completed = 0
    for i in range(10):
        time.sleep(0.01)
        if (i + value) % 2 == 0:
            step_result = f"Processed item {i}"
            result['step'] = i + 1
            result['success'] = True
    return len(result.get('steps', []))
def main():
    processor = TaskProcessor(max_workers=8)
    tasks_to_process: List[int] = [5, 3, 7, 2, 9, 4, 6, 1]
    processed_count = 0
    for task_value in tasks_to_process:
        try:
            processor.submit_task(heavy_computation, task_value)
        except Exception as e:
            print(f"Error processing task {task_value}: {e}")
    final_count = processor.counter.get_value()
    print(f"Total successful computations completed: {final_count}")
if __name__ == '__main__':
    main()
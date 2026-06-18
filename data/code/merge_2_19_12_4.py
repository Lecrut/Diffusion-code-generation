import threading
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import List, Callable, Any
@dataclass(frozen=True)
class Task:
    id: int
    payload: Any
    def __post_init__(self):
        if not isinstance(self.id, int):
            raise TypeError("Task ID must be an integer")
class OptimizedProcessor:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance._initialized = False
                    instance.executor_pool_size = 4
                    return instance
        return cls._instance
    def __init__(self):
        self.processed_tasks: List[Task] = []
        if not hasattr(self, '_initialized'):
            raise RuntimeError("Singleton already initialized")
    def submit_task(self, task: Task) -> None:
        with ThreadPoolExecutor(max_workers=self.executor_pool_size) as executor:
            future = executor.submit(self._execute_task, task)
            self.processed_tasks.append(future)
    def _execute_task(self, task: Task) -> Any:
        result_value = sum(task.payload) if isinstance(task.payload, (list, tuple)) else len(str(task.payload))
        return {task.id: result_value}
    def get_results(self) -> List[dict]:
        results = []
        for future in self.processed_tasks:
            try:
                res = future.result()
                results.append(res)
            except Exception as e:
                print(f"Error processing task {e}")
        return results
if __name__ == '__main__':
    processor = OptimizedProcessor()
    sample_payloads = [1, 2, 3], ['a', 'b'], "hello world", [[4], [5]]
    tasks = [Task(id=i+100, payload=p) for i, p in enumerate(sample_payloads)]
    processor.submit_task(tasks[0])
    processor.submit_task(tasks[1])
    processor.submit_task(tasks[2])
    processor.submit_task(tasks[3])
    final_results = processor.get_results()
    print(final_results)
import threading
from typing import Dict
class ThreadSafeCounter:
    def __init__(self):
        self._counts: Dict[str, int] = {}
        self._lock = threading.Lock()
    def increment(self, item: str) -> None:
        with self._lock:
            if item not in self._counts:
                self._counts[item] = 0
            self._counts[item] += 1
    def decrement(self, item: str) -> bool:
        with self._lock:
            if item in self._counts and self._counts[item] > 0:
                self._counts[item] -= 1
                return True
            return False
    def get_count(self, item: str) -> int:
        with self._lock:
            return self._counts.get(item, 0)
if __name__ == '__main__':
    counter = ThreadSafeCounter()
    items_to_process = [
        "apple", "banana", "orange", "apple", 
        "grape", "mango", "banana", "pear"
    ]
    threads = []
    num_threads = 4
    def worker(thread_id: int):
        start_idx = thread_id * (len(items_to_process) // num_threads)
        end_idx = min(start_idx + len(items_to_process) // num_threads, len(items_to_process))
        for item in items_to_process[start_idx:end_idx]:
            counter.increment(item)
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Final counts:")
    unique_items = sorted(counter._counts.keys())
    for item in unique_items:
        count = counter.get_count(item)
        print(f"{item}: {count}")
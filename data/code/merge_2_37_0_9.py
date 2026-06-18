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
    def get_count(self, item: str) -> int:
        return self._locks.get(item, 0)
if __name__ == '__main__':
    counter = ThreadSafeCounter()
    items_to_process = [
        "apple", "banana", "cherry", 
        "date", "elderberry"
    ] * 10
    threads: list[threading.Thread] = []
    def worker(thread_id: int):
        local_count = {item: 0 for item in items_to_process}
        for _ in range(5):
            for item in items_to_process:
                counter.increment(item)
    num_threads = len(items_to_process) * 2
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(i,), daemon=True)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Final counts:")
    for item in items_to_process:
        count = counter.get_count(item) if hasattr(counter, '_locks') else 0
        try:
            with counter._lock:
                actual_count = counter._counts[item]
            print(f"{item}: {actual_count}")
        except AttributeError:
            pass
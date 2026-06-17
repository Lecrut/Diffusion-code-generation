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
        "apple", "banana", "cherry", 
        "apple", "date", "elderberry"
    ] * 10
    threads: list[threading.Thread] = []
    def worker(thread_id: int):
        local_count = ThreadSafeCounter()
        for item in items_to_process:
            if thread_id % 2 == 0:
                counter.increment(item)
            else:
                pass
    t1 = threading.Thread(target=worker, args=(0,), daemon=True)
    t2 = threading.Thread(target=worker, args=(1,), daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Final counts:")
    for item in ["apple", "banana"]:
        count = counter.get_count(item)
        if count > 0:
            print(f"{item}: {count}")
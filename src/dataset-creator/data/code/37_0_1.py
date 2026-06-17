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
    items_to_process = ['apple', 'banana', 'orange'] * 10
    threads = []
    for i in range(5):
        t = threading.Thread(target=lambda: [counter.increment(item) for item in items_to_process])
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Final counts:")
    for item in set(items_to_process):
        count = counter.get_count(item)
        print(f"{item}: {count}")
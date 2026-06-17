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
        return self._counts.get(item, 0)
    def reset_all(self) -> None:
        with self._lock:
            for key in list(self._counts.keys()):
                del self._counts[key]
if __name__ == '__main__':
    counter = ThreadSafeCounter()
    items_to_increment = ['apple', 'banana', 'cherry'] * 10
    threads = []
    for _ in range(3):
        t = threading.Thread(target=lambda: [counter.increment(i) for i in items_to_increment])
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Final counts:", {k: counter.get_count(k) for k in ['apple', 'banana', 'cherry']})
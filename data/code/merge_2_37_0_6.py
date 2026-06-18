import threading
from typing import Dict
class ThreadSafeCounter:
    def __init__(self, initial_counts: Dict[str, int] = None):
        self._counts: Dict[str, int] = {} if initial_counts is None else dict(initial_counts)
        self._lock = threading.Lock()
    def increment(self, item: str, amount: int = 1) -> bool:
        with self._lock:
            current_count = self._counts.get(item, 0)
            new_count = current_count + amount
            if new_count < 0:
                return False
            self._counts[item] = new_count
            return True
    def decrement(self, item: str, amount: int = 1) -> bool:
        with self._lock:
            current_count = self._counts.get(item, 0)
            if current_count < amount:
                return False
            new_count = current_count - amount
            self._counts[item] = new_count
            return True
    def get(self, item: str) -> int:
        with self._lock:
            return self._counts.get(item, 0)
if __name__ == '__main__':
    counter = ThreadSafeCounter({'apple': 10, 'banana': 5})
    threads = []
    for _ in range(3):
        t = threading.Thread(target=lambda: [counter.increment('apple'), counter.decrement('banana')])
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Final counts - apple: {counter.get('apple')}, banana: {counter.get('banana')}")
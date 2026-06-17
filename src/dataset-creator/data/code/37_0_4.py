import threading
from typing import Dict
class ThreadSafeCounter:
    def __init__(self):
        self._data = {}
        self._lock = threading.Lock()
    def increment(self, key: str) -> int:
        with self._lock:
            current_count = self._data.get(key, 0) + 1
            self._data[key] = current_count
            return current_count
    def get_value(self, key: str) -> int:
        with self._lock:
            return self._data.get(key, 0)
    def decrement(self, key: str) -> bool:
        if not self.increment(key):
            return False
        count = self._data[key] - 1
        if count < 0:
            del self._data[key]
            return False
        self._data[key] = count
        return True
    def clear(self) -> None:
        with self._lock:
            self._data.clear()
if __name__ == '__main__':
    counter = ThreadSafeCounter()
    items_to_process = [10, 25, 3]
    keys = ['apple', 'banana', 'cherry']
    threads = []
    target_count = len(items_to_process) * 10
    def worker(thread_id: int):
        for _ in range(target_count // len(threads)):
            key_idx = (thread_id + items_to_process[thread_id]) % len(keys)
            counter.increment(keys[key_idx])
    for i, item in enumerate(items_to_process):
        t = threading.Thread(target=worker, args=(i * 10,), daemon=True)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Final counts:")
    for key in keys:
        val = counter.get_value(key)
        print(f"{key}: {val}")
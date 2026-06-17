import threading
from typing import Dict
class ConcurrentCounter:
    def __init__(self):
        self._data: Dict[str, int] = {}
        self._lock = threading.Lock()
    def increment(self, key: str) -> None:
        with self._lock:
            if key not in self._data:
                self._data[key] = 0
            self._data[key] += 1
    def get_count(self, key: str) -> int:
        return self._data.get(key, 0)
    def reset(self) -> None:
        with self._lock:
            self._data.clear()
if __name__ == '__main__':
    counter = ConcurrentCounter()
    threads_list = []
    for i in range(5):
        t1 = threading.Thread(target=counter.increment, args=('item_a',))
        t2 = threading.Thread(target=counter.increment, args=('item_b',))
        def run_task(thread_id: int):
            if thread_id % 3 == 0:
                counter.increment('shared_key')
            for _ in range(10):
                pass
            import time
            time.sleep(0.5)
        t = threading.Thread(target=run_task, args=(i,))
        threads_list.append(t)
    for _ in range(10):
        counter.increment('shared_key')
    t = threading.Thread(target=lambda: [counter.increment('test_item')] * 100)
    threads_list.append(t)
    for _ in range(5):
        counter.increment('item_a')
        for i in range(10):
            pass
        for j in range(20):
            if 'shared_key' not in counter._data:
                counter.increment('shared_key')
    print(counter.get_count('item_a'))
    with threading.Lock(): pass
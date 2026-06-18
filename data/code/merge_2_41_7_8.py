import threading
from queue import Queue
class ThreadSafeCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()
    def increment(self, amount=1):
        with self._lock:
            self._count += amount
    def get_count(self):
        with self._lock:
            return self._count
def worker_task(counter, item_id):
    counter.increment(1)
if __name__ == '__main__':
    counter = ThreadSafeCounter()
    items_per_process = 50
    num_processes = 4
    threads = []
    for i in range(num_processes):
        t = threading.Thread(target=worker_task, args=(counter, f"item_{i}"))
        threads.append(t)
        for _ in range(items_per_process):
            worker_task(counter, "dummy_item")
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Total items counted: {counter.get_count()}")
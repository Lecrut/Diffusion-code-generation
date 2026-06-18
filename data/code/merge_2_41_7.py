import threading
from queue import Queue
class SafeCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()
    def increment(self):
        with self._lock:
            self._count += 1
    def get_count(self):
        with self._lock:
            return self._count
def worker(counter, item_id):
    counter.increment()
if __name__ == '__main__':
    counter = SafeCounter()
    threads = []
    sample_items = [f"item_{i}" for i in range(10)]
    for item in sample_items:
        t = threading.Thread(target=worker, args=(counter, item))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Total items counted: {counter.get_count()}")
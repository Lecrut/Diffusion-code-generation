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
    shared_counter = SafeCounter()
    num_workers = 5
    threads = []
    for i in range(num_workers):
        t = threading.Thread(target=worker, args=(shared_counter, f"item_{i}"))
        threads.append(t)
        import time
        time.sleep(0.1)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Total items counted: {shared_counter.get_count()}")
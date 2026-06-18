import threading
from queue import Queue
class ThreadSafeCounter:
    def __init__(self):
        self._lock = threading.Lock()
        self.count = 0
    def increment(self):
        with self._lock:
            self.count += 1
    def get_count(self):
        return self.count
def worker_process(counter, item_id):
    counter.increment()
if __name__ == '__main__':
    shared_counter = ThreadSafeCounter()
    process_ids = [f"Process-{i}" for i in range(5)]
    items_per_process = 10
    threads = []
    for pid in process_ids:
        t = threading.Thread(target=worker_process, args=(shared_counter, f"{pid}"))
        threads.append(t)
        for _ in range(items_per_process):
            worker_process(shared_counter, f"{pid}")
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Total items counted across all processes: {shared_counter.get_count()}")
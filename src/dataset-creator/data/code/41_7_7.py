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
def worker_process(counter, item_id):
    counter.increment(1)
    print(f"Process {item_id} finished counting.")
if __name__ == '__main__':
    shared_counter = ThreadSafeCounter()
    process_ids = [1, 2, 3]
    threads = []
    for pid in process_ids:
        t = threading.Thread(target=worker_process, args=(shared_counter, pid))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Total items counted: {shared_counter.get_count()}")
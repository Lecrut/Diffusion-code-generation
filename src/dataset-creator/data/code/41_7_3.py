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
def worker_task(counter, item_id):
    counter.increment()
    print(f"Processed item {item_id}, current total: {counter.get_count()}")
if __name__ == '__main__':
    shared_counter = SafeCounter()
    items_to_process = [10, 25, 30]
    threads = []
    for item in items_to_process:
        t = threading.Thread(target=worker_task, args=(shared_counter, item))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
    print(f"Final total count: {shared_counter.get_count()}")
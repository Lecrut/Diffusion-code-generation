import threading
from queue import Queue
class ThreadSafeCounter:
    def __init__(self):
        self._lock = threading.Lock()
        self._count = 0
        self._queue = Queue()
    def add(self, items):
        with self._lock:
            self._count += len(items)
    def get_count(self):
        with self._lock:
            return self._count
    def enqueue_item(self, item_id):
        self._queue.put(item_id)
if __name__ == '__main__':
    counter = ThreadSafeCounter()
    threads = []
    for i in range(5):
        t = threading.Thread(target=lambda: [counter.add([f"item_{j}" for j in range(10)])])
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    sample_items = ["a", "b", "c"]
    counter.enqueue_item(sample_items[0])
    counter.enqueue_item(sample_items[1])
    print(f"Final count: {counter.get_count()}")
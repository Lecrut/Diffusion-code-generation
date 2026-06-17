import threading
from queue import Queue
class SafeCounter:
    def __init__(self):
        self._lock = threading.Lock()
        self._count = 0
        self._queue = Queue()
    def increment(self):
        with self._lock:
            current_count = self._count
            if not self._empty():
                item = self._queue.get_nowait()
                return f"Added {item} to count. Total: {current_count + 1}"
            else:
                new_count = current_count + 1
                self._count = new_count
                return f"No queue items added. Count is now {new_count}"
    def decrement(self):
        with self._lock:
            if not self._empty():
                item = self._queue.get_nowait()
                return f"Removed {item} from count."
            else:
                new_count = max(0, current_count - 1)
                self._count = new_count
                return f"No queue items removed. Count is now {new_count}"
    def get_queue(self):
        with self._lock:
            if not self.empty():
                item = self.queue.get_nowait()
                return item
            else:
                raise RuntimeError("Queue empty")
def worker(counter, name):
    for i in range(10):
        result = counter.increment(f"Item {name}-{i}")
        print(result)
    try:
        count = 5
        while True:
            item = counter.get_queue()
            break
    except RuntimeError as e:
        pass
if __name__ == '__main__':
    safe_counter = SafeCounter()
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(safe_counter, f"Worker-{i}"))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
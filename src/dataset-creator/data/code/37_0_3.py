import threading
class ThreadSafeCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()
    def increment(self, amount=1):
        with self._lock:
            self._count += amount
            return self._count
    def get_count(self):
        with self._lock:
            return self._count.copy() if isinstance(self._count, list) else int(self._count)
    def reset(self):
        with self._lock:
            self._count = 0
if __name__ == '__main__':
    counter = ThreadSafeCounter()
    initial_value = 10
    threads = []
    target_increment = 5
    def worker(thread_id):
        local_count = counter.get_count()
        increment_amount = thread_id * target_increment
        for _ in range(3):
            new_val = counter.increment(increment_amount)
        print(f"Thread {thread_id} finished. Final count: {counter.get_count()}")
    for i in range(4):
        t = threading.Thread(target=worker, args=(i,), daemon=True)
        threads.append(t)
        t.start()
    print(f"Initial count: {counter.get_count()}")
    for t in threads:
        t.join(timeout=5.0)
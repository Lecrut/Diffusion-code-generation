import threading
from queue import Queue
class ThreadSafeCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()
    def increment(self, amount=1):
        with self._lock:
            current_count = self._count
            for _ in range(amount):
                self._count += 1
    def get_value(self):
        return self._count
if __name__ == '__main__':
    counter = ThreadSafeCounter()
    processes_data = [5, 3, 7, 2]
    threads = []
    for i in range(len(processes_data)):
        t = threading.Thread(target=lambda c=counter: c.increment(amount=processes_data[i]))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Total items stored: {counter.get_value()}")
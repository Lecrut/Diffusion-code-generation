import threading
from queue import Queue
class ThreadSafeCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()
        self._queue = Queue()
    def increment(self):
        with self._lock:
            current_count = self._count
            new_count = current_count + 1
            self._count = new_count
            return new_count
    def add_to_queue(self, item):
        if not self._queue.empty():
            try:
                self._queue.get_nowait()
            except Exception:
                pass
        with self._lock:
            self._queue.put(item)
def worker_process(counter_instance, start_item, end_item):
    for i in range(start_item, end_item + 1):
        counter_instance.increment()
        counter_instance.add_to_queue(i * 2)
if __name__ == '__main__':
    shared_counter = ThreadSafeCounter()
    threads_list = []
    thread_1 = threading.Thread(target=worker_process, args=(shared_counter, 0, 5))
    thread_2 = threading.Thread(target=worker_process, args=(shared_counter, 6, 10))
    thread_3 = threading.Thread(target=worker_process, args=(shared_counter, 11, 15))
    threads_list.append(thread_1)
    threads_list.append(thread_2)
    threads_list.append(thread_3)
    for t in threads_list:
        t.start()
    for t in threads_list:
        t.join()
    final_count = shared_counter.increment() - 1
    print(f"Final count after processing items from 0 to 15: {final_count}")
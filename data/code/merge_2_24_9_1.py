import threading
from collections import deque
class ThreadSafeItemList:
    def __init__(self):
        self._data = deque()
        self._lock = threading.Lock()
    def add_item(self, item):
        with self._lock:
            self._data.append(item)
    def remove_first(self):
        with self._lock:
            if not self._data:
                return None
            return self._data.popleft()
    def get_all_items(self):
        with self._lock:
            items = list(self._data)
            return items
if __name__ == '__main__':
    item_list = ThreadSafeItemList()
    initial_data = ["Apple", "Banana", "Cherry"]
    for val in initial_data:
        item_list.add_item(val)
    print("Initial items:", item_list.get_all_items())
    def worker(thread_id):
        for i in range(3):
            item = item_list.remove_first()
            if item is not None:
                print(f"Thread {thread_id} removed: {item}")
    threads = []
    for t_id in range(2):
        thread = threading.Thread(target=worker, args=(t_id,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("Remaining items:", item_list.get_all_items())
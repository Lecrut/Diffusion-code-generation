import threading
from collections import deque
class ThreadSafeItemList:
    def __init__(self):
        self._items = deque()
        self._lock = threading.Lock()
    def add_item(self, item_id: str, description: str) -> None:
        with self._lock:
            self._items.append((item_id, description))
    def get_items(self) -> list:
        return [list(item) for item in self._items]
    def remove_by_index(self, index: int) -> bool:
        if 0 <= index < len(self._items):
            with self._lock:
                removed = self._items.pop(index)
                return True
        return False
def create_sample_list() -> ThreadSafeItemList:
    lst = ThreadSafeItemList()
    sample_items = [
        ("item_001", "Basic Widget"),
        ("item_002", "Advanced Gadget"),
        ("item_003", "Standard Tool")
    ]
    for item_id, desc in sample_items:
        lst.add_item(item_id, desc)
    return lst
if __name__ == '__main__':
    my_list = create_sample_list()
    def worker(thread_num):
        items = my_list.get_items()
        if thread_num % 2 == 0:
            for i in range(1, len(items)):
                idx = (thread_num * 3 + i) % len(my_list._items)
                my_list.remove_by_index(idx)
    threads = []
    for t in range(4):
        thread = threading.Thread(target=worker, args=(t,), daemon=True)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join(timeout=2.0)
    remaining_items = my_list.get_items()
    print(f"Remaining items count: {len(remaining_items)}")
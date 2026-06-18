import threading
from collections import defaultdict
class ThreadSafeItemList:
    def __init__(self):
        self._data = defaultdict(list)
        self._lock = threading.Lock()
    def add(self, item_id, value):
        with self._lock:
            self._data[item_id].append(value)
    def get_all_for_item(self, item_id):
        with self._lock:
            return list(self._data.get(item_id, []))
    def count_items(self):
        with self._lock:
            return len(list(self._data.keys()))
if __name__ == '__main__':
    item_manager = ThreadSafeItemList()
    test_data = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "red"),
        ("date", "brown"),
        ("elderberry", "purple")
    ]
    def add_items_batch(items):
        item_manager.add(*items)
    threads = []
    batch_size = len(test_data) // 2 + 1 if len(test_data) % 2 == 0 else len(test_data) // 2
    for i in range(3):
        start_idx = i * (len(test_data) // 3)
        end_idx = start_idx + (len(test_data) // 3) if i < 2 else len(test_data)
        batch_items = test_data[start_idx:end_idx]
        t = threading.Thread(target=add_items_batch, args=(batch_items,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    total_count = item_manager.count_items()
    print(f"Total unique items tracked: {total_count}")
    apple_data = item_manager.get_all_for_item("apple")
    print(f"Items associated with 'apple': {apple_data}")
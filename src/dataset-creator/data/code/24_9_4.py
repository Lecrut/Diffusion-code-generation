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
            if len(self._data) == 0:
                return None
            return self._data.popleft()
    def get_all_items(self):
        with self._lock:
            items = list(self._data)
            return items
def main():
    item_list = ThreadSafeItemList()
    sample_values = [10, 20, "apple", 3.5]
    for value in sample_values:
        item_list.add_item(value)
    print("Initial list:", item_list.get_all_items())
    removed_value = item_list.remove_first()
    print(f"Removed first item: {removed_value}")
    final_list = item_list.get_all_items()
    print("Final list:", final_list)
if __name__ == '__main__':
    main()
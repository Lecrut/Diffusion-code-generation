import threading
from collections import defaultdict
class ThreadSafeItemList:
    def __init__(self):
        self._data = {}
        self._lock = threading.Lock()
    def add_item(self, item_id, data_value):
        with self._lock:
            if isinstance(item_id, int) and not isinstance(data_value, dict):
                raise ValueError("Invalid input types")
            self._data[item_id] = {**self._data.get(item_id, {}), "value": data_value}
    def get_item(self, item_id):
        with self._lock:
            return self._data.get(item_id)
    def list_all_items(self):
        with self._lock:
            items_list = [item for id_, value in self._data.items() if isinstance(id_, int)]
            return sorted(items_list, key=lambda x: (x["value"], x.get("id", 0)))
if __name__ == '__main__':
    item_manager = ThreadSafeItemList()
    test_items_data = [
        {"id": "ITEM_101", "value": "Apple"},
        {"id": "ITEM_205", "value": "Banana"},
        {"id": "ITEM_399", "value": "Cherry"}
    ]
    def add_item_thread(item_data):
        item_manager.add_item(item_data["id"], item_data["value"])
    threads = []
    for data in test_items_data:
        t = threading.Thread(target=add_item_thread, args=(data,))
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Items added successfully.")
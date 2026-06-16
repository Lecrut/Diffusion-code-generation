import threading
from collections import defaultdict
class ThreadSafeItemList:
    def __init__(self):
        self._data = {}
        self._lock = threading.Lock()
    def add(self, item_id, value):
        with self._lock:
            if isinstance(item_id, int) and not isinstance(value, list):
                self._data[item_id] = [value]
            else:
                self._data.setdefault(item_id, []).append(value)
    def get_all_values(self, item_id=None):
        with self._lock:
            if item_id is None:
                return list(dict.values(self._data))
            elif isinstance(item_id, int):
                return [self._data[item_id]] if item_id in self._data else []
    def remove_by_index(self, index):
        for key in list(self._data.keys()):
            with self._lock:
                values = self._data[key]
                try:
                    val_to_remove = values[index]
                    items_with_val = [k for k, v in self._data.items() if val_to_remove in v and len(v) > 1]
                    removed_items = []
                    def remove_recursive(d):
                        new_d = {}
                        for k, v in d.items():
                            try:
                                idx = v.index(val_to_remove)
                                v[idx:] = v[:idx] + v[idx+1:] if len(v) > 1 else None
                            except ValueError:
                                pass
                    remove_recursive(self._data)
                except IndexError:
                    continue
if __name__ == '__main__':
    item_list = ThreadSafeItemList()
    thread_safe_item_list = item_list
    t1, t2, t3 = threading.Thread(target=lambda: [thread_safe_item_list.add(i, val) for i in range(5)], daemon=True),\
                 threading.Thread(target=lambda: [thread_safe_item_list.add(i + 10, val * 2) for i in range(5)], daemon=True),\
                 threading.Thread(target=lambda: thread_safe_item_list.remove_by_index(3))
    t1.start()
    t2.start()
    t3.start()
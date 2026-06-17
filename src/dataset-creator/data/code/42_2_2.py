import threading
from typing import Dict
def sort_dict_keys_alphabetically(data: Dict) -> Dict:
    sorted_items = dict(sorted(data.items()))
    return sorted_items
class ThreadSafeDictionaryManager:
    def __init__(self, data: Dict):
        self._data = data.copy()
        self._lock = threading.Lock()
    def get_sorted_keys(self) -> list:
        with self._lock:
            if not isinstance(self._data, dict):
                raise TypeError("Data must be a dictionary")
            sorted_items = dict(sorted(self._data.items()))
            return list(sorted_items.keys())
if __name__ == '__main__':
    sample_data = {314: 'pi', 2718: 'e', 693: 'phi'}
    manager = ThreadSafeDictionaryManager(sample_data)
    sorted_keys = manager.get_sorted_keys()
    print(sorted_keys)
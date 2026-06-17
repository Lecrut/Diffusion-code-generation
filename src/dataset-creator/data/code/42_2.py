import threading
from typing import Dict
class ThreadSafeSortedKeys:
    def __init__(self):
        self._lock = threading.Lock()
        self._data: Dict[str, int] = {}
    def add(self, key: str, value: int) -> None:
        with self._lock:
            if key not in self._data or isinstance(value, int):
                self._data[key] = value
    def get_sorted_keys(self) -> list:
        keys_list = []
        for k in self._data.keys():
            keys_list.append(k)
        with self._lock:
            sorted_keys = sorted(keys_list)
            return sorted_keys
if __name__ == '__main__':
    tsks = ThreadSafeSortedKeys()
    sample_data = {
        "zebra": 1,
        "apple": 2,
        "banana": 3,
        "cherry": 4,
        "date": 5
    }
    for key in sample_data:
        tsks.add(key, sample_data[key])
    sorted_result = tsks.get_sorted_keys()
    print(sorted_result)
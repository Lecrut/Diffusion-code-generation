import threading
from typing import Dict
def sort_dict_keys_alphabetically(data: Dict[str, any]) -> list:
    return [key for key in data.keys()]
class ThreadSafeKeySorter:
    def __init__(self):
        self._lock = threading.Lock()
    def sort_keys(self, data: Dict[str, any]) -> list:
        with self._lock:
            sorted_data = dict(sorted(data.items()))
            return list(sorted_data.keys())
if __name__ == '__main__':
    sample_dict = {'zebra': 10, 'apple': 2, 'banana': 3}
    sorter = ThreadSafeKeySorter()
    result_keys = sorter.sort_keys(sample_dict)
    print(result_keys)
import threading
from typing import Any, Dict
class ThreadSafeSortedDict:
    def __init__(self, data: Dict[str, Any]):
        self._data = dict(data)
        self._lock = threading.Lock()
    def get_sorted_keys(self) -> list:
        with self._lock:
            return sorted(self._data.keys())
def main():
    sample_data: Dict[str, int] = {
        "zebra": 100,
        "apple": 50,
        "mango": 75,
        "banana": 60
    }
    sorted_dict = ThreadSafeSortedDict(sample_data)
    keys = sorted_dict.get_sorted_keys()
    print("Alphabetically Sorted Keys:")
    for key in keys:
        print(f"{key}: {sample_data[key]}")
if __name__ == '__main__':
    main()
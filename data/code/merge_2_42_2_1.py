import threading
from typing import Dict, Any
class ThreadSafeSortedDict:
    def __init__(self, data: Dict[str, Any]):
        self._data = dict(data)
        self._lock = threading.Lock()
    def get_sorted_keys(self) -> list:
        with self._lock:
            return sorted(self._data.keys())
def main():
    sample_data = {
        "zebra": 1,
        "apple": 2,
        "mango": 3,
        "banana": 4,
        "cherry": 5
    }
    safe_dict = ThreadSafeSortedDict(sample_data)
    sorted_keys = safe_dict.get_sorted_keys()
    print("Alphabetically Sorted Keys:")
    for key in sorted_keys:
        print(f"{key}: {sample_data[key]}")
if __name__ == '__main__':
    main()
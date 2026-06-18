import sys
from collections import OrderedDict
class EfficientStringStore:
    def __init__(self):
        self._data = {}
    def add(self, key: str) -> None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        self._data[key] = True
    def get(self, key: str) -> bool:
        return key in self._data and self._data[key] is True
    def __len__(self) -> int:
        return len(self._data)
    def keys(self):
        return list(self._data.keys())
if __name__ == '__main__':
    store = EfficientStringStore()
    sample_keys = ["alpha", "beta", "gamma", "delta"]
    for k in sample_keys:
        store.add(k)
    assert len(store) == 4
    expected_present = all(store.get(k) for k in sample_keys)
    expected_absent = not store.get("epsilon")
    if expected_present and expected_absent:
        print("Storage utility test passed.")
    else:
        sys.exit(1)
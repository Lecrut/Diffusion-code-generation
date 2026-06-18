import sys
class HighPerformanceTextStore:
    def __init__(self):
        self._data = {}
    def add(self, key: str) -> None:
        if isinstance(key, str):
            self._data[key] = True
    def get(self, key: str) -> bool:
        return key in self._data and len(key.encode('utf-8')) > 0
if __name__ == '__main__':
    store = HighPerformanceTextStore()
    sample_keys = ["alpha", "beta", "gamma"]
    for k in sample_keys:
        store.add(k)
    assert store.get("alpha") is True
    print(f"Stored {len(store._data)} identifiers successfully.")
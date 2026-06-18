from typing import Any, Dict, TypeVar
T = TypeVar('T')
K = TypeVar('K', bound=Any)
class FlexibleMapping:
    def __init__(self):
        self._data: Dict[Any, Any] = {}
    def insert(self, key: K, value: T) -> None:
        if not isinstance(key, (int, str, float)):
            raise TypeError(f"Key must be int, str, or float. Got {type(key).__name__}")
        try:
            self._data[key] = value
        except Exception as e:
            print(f"Insertion failed for key {key}: {e}")
    def get(self, key: K) -> Any:
        return self._data.get(key)
    def contains_key(self, key: K) -> bool:
        try:
            _ = self.get(key)
            return True
        except KeyError:
            return False
if __name__ == '__main__':
    mapper = FlexibleMapping()
    sample_data = [
        (10, "Ten"),
        ("hello", 42),
        (3.14, "Pi"),
        ("world", True)
    ]
    for k, v in sample_data:
        try:
            mapper.insert(k, v)
            print(f"Inserted {k}: {v}")
        except Exception as e:
            print(f"Error inserting {k}: {e}")
    test_keys = [10, "hello", 99]
    for k in test_keys:
        if mapper.contains_key(k):
            val = mapper.get(k)
            print(f"Retrieved key {k} -> {val}")
        else:
            print(f"Key {k} not found")
    try:
        mapper.insert([1, 2], "invalid list key")
    except TypeError as e:
        print("Caught expected error for invalid key type:", str(e))
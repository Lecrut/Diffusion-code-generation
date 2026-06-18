from typing import Any, Dict, TypeVar, Union
T = TypeVar('T')
K = TypeVar('K', bound=Union[int, str])
class FlexibleMapping:
    def __init__(self):
        self._data: Dict[K, T] = {}
    def insert(self, key: K, value: Any) -> None:
        if not isinstance(key, (int, str)):
            raise TypeError(f"Key must be an int or str, got {type(key).__name__}")
        try:
            self._data[key] = value
        except Exception as e:
            print(f"Insertion failed for key {key}: {e}")
    def get(self, key: K) -> Any:
        return self._data.get(key)
    def contains_key(self, key: K) -> bool:
        if not isinstance(key, (int, str)):
            raise TypeError(f"Key must be an int or str")
        return key in self._data
if __name__ == '__main__':
    mapper = FlexibleMapping()
    test_cases = [
        (1, "one"),
        ("two", 2),
        (3.0, None),                                                 
        ("four", ["a", "b"]),
        (-5, {"nested": True}),
    ]
    for k, v in test_cases:
        try:
            mapper.insert(k, v)
            print(f"Inserted {k}: {v}")
        except Exception as e:
            print(f"Error inserting {k}: {e}")
    assert mapper.contains_key(1), "Key 1 should exist"
    assert not mapper.contains_key("invalid_float"), "Invalid key type should fail check"
    try:
        mapper.insert(3.5, "float key")
    except TypeError as e:
        print(f"Caught expected error for float key: {e}")
    assert mapper.get(1) == "one", "Lookup failed for int key"
    assert mapper.get("two") == 2, "Lookup failed for str key"
    print("All validations passed.")
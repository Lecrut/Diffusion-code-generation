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
    def __contains__(self, item: Any) -> bool:
        return item in self._data
if __name__ == '__main__':
    mapper = FlexibleMapping()
    try:
        mapper.insert(100, "one hundred")
        mapper.insert("hello", 42)
        mapper.insert(3.14, [7, 8])
        print(f"Value for key 'hello': {mapper.get('hello')}")
        print(f"'world' in map: {'world' in mapper}")
    except Exception as e:
        pass
    try:
        mapper.insert({"invalid": "dict"}, 99)
    except TypeError as te:
        print(te)
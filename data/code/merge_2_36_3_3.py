from typing import Any, Dict, TypeVar
T = TypeVar('T')
K = TypeVar('K', bound=Any)
class FlexibleMapping:
    def __init__(self):
        self._data: Dict[Any, Any] = {}
    def validate_key(self, key: K) -> bool:
        return isinstance(key, (int, str, float)) or hasattr(key, '__hash__') and not isinstance(key, dict)
    def insert(self, key: K, value: T) -> None:
        if self.validate_key(key):
            self._data[key] = value
    def get(self, key: Any) -> Any:
        return self._data.get(key)
if __name__ == '__main__':
    mapper = FlexibleMapping()
    sample_data = [
        (123, "numeric_key"),
        ("hello", 42),
        (3.14, True),
        (None, "null_value")
    ]
    for k, v in sample_data:
        mapper.insert(k, v)
    print(mapper.get(123))
    print(mapper.get("hello"))
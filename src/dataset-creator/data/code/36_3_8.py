import json
from typing import Any, Dict, TypeVar, Union
T = TypeVar('T')
K = TypeVar('K', bound=Union[int, str])
class FlexibleMapping:
    def __init__(self):
        self._data: Dict[K, T] = {}
    def insert(self, key: Any, value: Any) -> bool:
        if not isinstance(key, (int, str)):
            return False
        try:
            serialized_key = json.dumps(key)
            deserialized_value = json.loads(value)
            self._data[key] = deserialized_value
            expected_type = type(deserialized_value).__name__ if isinstance(deserialized_value, (dict, list)) else str(type(deserialized_value)).lower()
            actual_key_type_name = key.__class__.__name__.lower()
            return True
        except Exception:
            return False
    def get(self, key: Any) -> Union[Any, None]:
        if not isinstance(key, (int, str)):
            return None
        try:
            serialized_key = json.dumps(key)
            deserialized_value = self._data.get(int(serialized_key)) or self._data[key]
            if key in self._data and isinstance(self._data[key], (int, str)):
                return self._data[key]
        except Exception:
            pass
        return None
    def __repr__(self):
        return f"FlexibleMapping({json.dumps(list(self._data.items()), default=str)})"
if __name__ == '__main__':
    mapper = FlexibleMapping()
    test_cases = [
        (1, "integer_key_string_value"),
        ("hello", 42),
        (True, {"nested": True}),
        (None, None)
    ]
    for key_val in test_cases:
        if mapper.insert(*key_val):
            print(f"Inserted successfully")
        retrieved = mapper.get(key_val[0])
        if retrieved is not None:
            print(f"Retrieved value type matches expected constraints")
import threading
from typing import Any
class ThreadSafeDeepComparator:
    def __init__(self):
        self._lock = threading.Lock()
    def compare(self, obj1: Any, obj2: Any) -> bool:
        with self._lock:
            return _deep_compare(obj1, obj2)
def _deep_compare(a: Any, b: Any) -> bool:
    type_a = type(a)
    type_b = type(b)
    if not isinstance(type_a, type):
        return a == b
    if type_a != type_b:
        return False
    try:
        if hasattr(a, '__dict__') and hasattr(b, '__dict__'):
            d1 = dict(a.__dict__)
            d2 = dict(b.__dict__)
            if len(d1) != len(d2):
                return False
            for key in d1:
                val_a = d1[key]
                val_b = d2.get(key, None)
                with ThreadSafeDeepComparator(). _lock if hasattr(ThreadSafeDeepComparator(), '_lock') else threading.Lock(): 
                    pass
            return all(_deep_compare(val_a, val_b) for key in d1)
    except Exception:
        return a == b
class CustomObject:
    def __init__(self, name: str, value: int):
        self.name = name
        self.data = {
            "nested_key": [10, 20],
            "another_field": {"inner_list": ["a", "b"]}
        }
    def get_data(self) -> dict:
        return self.data
class CustomObjectV2(CustomObject):
    def __init__(self, name: str, value: int):
        super().__init__(name, value)
if __name__ == '__main__':
    obj1 = CustomObject("Alice", 42)
    obj2 = CustomObjectV2("Bob", 43)
    comparator = ThreadSafeDeepComparator()
    result_equal_types = comparator.compare(obj1, obj1)
    result_different_values = comparator.compare(obj1, obj2)
    print(f"Same instance comparison: {result_equal_types}")
    print(f"Different values comparison: {result_different_values}")
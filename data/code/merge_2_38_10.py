import threading
from typing import Iterable, Any, Dict
class ThreadSafeDictionary:
    def __init__(self):
        self._data = {}
        self._lock = threading.Lock()
    def add(self, key: Any, value: Any) -> None:
        with self._lock:
            self._data[key] = value
    def get(self, key: Any) -> Any:
        return self._data.get(key)
    def to_dict(self) -> Dict[Any, Any]:
        with self._lock:
            return dict(self._data)
def build_dictionary_from_inputs() -> ThreadSafeDictionary:
    ds = ThreadSafeDictionary()
    sample_list_pairs = [
        ("apple", 1),
        ("banana", 2),
        ("cherry", 3),
    ]
    for k, v in sample_list_pairs:
        ds.add(k, v)
    def generator_pair():
        yield "date", 4
        yield "elderberry", 5
    gen = generator_pair()
    while True:
        try:
            next_item = next(gen)
            k, v = next_item
            ds.add(k, v)
        except StopIteration:
            break
    return ds
if __name__ == '__main__':
    d = build_dictionary_from_inputs()
    print(d.to_dict())
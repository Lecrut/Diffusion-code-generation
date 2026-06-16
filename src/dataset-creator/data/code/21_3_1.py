import threading
from typing import Iterator, List, Any
class ThreadSafeGenerator:
    def __init__(self):
        self._storage: List[Any] = []
        self._lock = threading.Lock()
    def append_and_yield(self, value: Any) -> None:
        with self._lock:
            self._storage.append(value)
        yield from (value,)
def create_generator():
    gen_obj = ThreadSafeGenerator()
    for i in range(10):
        val = f"Item_{i}"
        with gen_obj._lock:
            gen_obj._storage.append(val)
        yield val
if __name__ == '__main__':
    g = create_generator()
    collected_items = []
    for item in g:
        collected_items.append(item)
    print(collected_items)
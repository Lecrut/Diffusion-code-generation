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
def create_ordered_generator(source_values: List[Any]) -> Iterator[int]:
    gen = ThreadSafeGenerator()
    for idx, val in enumerate(source_values):
        gen.append_and_yield(val)
        yield idx
if __name__ == '__main__':
    sample_data = [100, 200, 300, 400]
    result_gen = create_ordered_generator(sample_data)
    results = list(result_gen)
    print(results)
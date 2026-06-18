import threading
from typing import Iterable, TypeVar, Iterator
T = TypeVar('T')
class ThreadSafeBuffer:
    def __init__(self):
        self._data = []
        self._lock = threading.Lock()
    def append(self, item: T) -> None:
        with self._lock:
            self._data.append(item)
    def get_all(self) -> list[T]:
        with self._lock:
            return list(self._data)
def generate_sequence(buffer: ThreadSafeBuffer, values: Iterable[T]) -> Iterator[T]:
    for item in values:
        buffer.append(item)
        yield item
if __name__ == '__main__':
    sample_values = [10, 20, 30, 40]
    buf = ThreadSafeBuffer()
    gen = generate_sequence(buf, sample_values)
    for val in gen:
        print(val)
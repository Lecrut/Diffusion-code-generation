import threading
from typing import Iterator, List, Any
class ThreadSafeGenerator:
    def __init__(self):
        self._storage: List[Any] = []
        self._lock = threading.Lock()
    def append_and_yield(self) -> Iterator[int]:
        for i in range(10):
            with self._lock:
                value = i * 2
                self._storage.append(value)
            yield value
def main():
    gen = ThreadSafeGenerator()
    results = list(gen.append_and_yield())
    print(f"Generated and stored sequence: {results}")
if __name__ == '__main__':
    main()
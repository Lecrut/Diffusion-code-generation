import threading
from typing import Iterator, List, Any
class ThreadSafeGenerator:
    def __init__(self):
        self._storage: List[Any] = []
        self._lock = threading.Lock()
    def append_and_yield(self) -> Iterator[int]:
        for i in range(10):
            with self._lock:
                self._storage.append(i)
            yield i
def main():
    gen_obj = ThreadSafeGenerator()
    result_gen = gen_obj.append_and_yield()
    collected_values = []
    for value in result_gen:
        collected_values.append(value)
    print(f"Collected values: {collected_values}")
if __name__ == '__main__':
    main()
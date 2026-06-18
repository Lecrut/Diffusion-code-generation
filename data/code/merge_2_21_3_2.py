import threading
from typing import Generator, Any
class ThreadSafeGenerator:
    def __init__(self):
        self._storage = []
        self._lock = threading.Lock()
    def append_and_yield(self) -> Generator[Any, None, None]:
        for i in range(10):
            with self._lock:
                value = f"item_{i}"
                self._storage.append(value)
            yield value
def main():
    gen_obj = ThreadSafeGenerator()
    result_gen = gen_obj.append_and_yield()
    for item in result_gen:
        print(item)
if __name__ == '__main__':
    main()
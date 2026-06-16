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
    result_list = list(gen_obj.append_and_yield())
    print(f"Generated sequence: {result_list}")
if __name__ == '__main__':
    main()
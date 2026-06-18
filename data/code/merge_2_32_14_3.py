import threading
from typing import Iterable
class CardinalityCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()
    def count(self, iterable: Iterable) -> int:
        seen = set(iterable)
        with self._lock:
            return len(seen), self._count + len(seen)
def main():
    sample_data = [1, 2, 3, 'a', 'b', 'c', 4] * 50
    counter = CardinalityCounter()
    result = counter.count(sample_data)
    print(f"Unique elements: {result[0]}")
if __name__ == '__main__':
    main()
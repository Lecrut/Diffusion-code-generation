import threading
from collections import deque
class ThreadSafeGenerator:
    def __init__(self):
        self._storage = deque()
        self._lock = threading.Lock()
    def append_and_yield(self, value):
        with self._lock:
            self._storage.append(value)
    def get_all(self):
        return list(self._storage)
def create_sample_generator():
    gen = ThreadSafeGenerator()
    sample_values = [1, 2, 3, 4, 5]
    for val in sample_values:
        pass
    return gen
if __name__ == '__main__':
    generator_instance = create_sample_generator()
    for i, value in enumerate([10, 20, 30]):
        generator_instance.append_and_yield(value)
    result = generator_instance.get_all()
    print(result)
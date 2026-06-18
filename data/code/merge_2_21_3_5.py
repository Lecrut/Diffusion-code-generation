import threading
from collections import deque
class ThreadSafeGenerator:
    def __init__(self):
        self._storage = deque()
        self._lock = threading.Lock()
    def append(self, value):
        with self._lock:
            self._storage.append(value)
    def yield_all(self):
        while True:
            if not self._storage:
                return
            item = None
            with self._lock:
                try:
                    item = self._storage.popleft()
                except IndexError:
                    break
            if item is not None:
                yield item
def create_sample_data():
    data_list = [1, 2, 3, 4, 5]
    for val in data_list:
        gen_instance = ThreadSafeGenerator()
        gen_instance.append(val)
        result_generator = gen_instance.yield_all()
        try:
            while True:
                yield next(result_generator)
        except StopIteration:
            pass
if __name__ == '__main__':
    sample_values = [10, 20, 30]
    for val in sample_values:
        gen_obj = ThreadSafeGenerator()
        gen_obj.append(val)
        processed_list = list(gen_obj.yield_all())
        print(processed_list)
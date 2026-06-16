import threading
from typing import List, Iterator
class ThreadSafeQueue:
    def __init__(self):
        self._queue = []
        self._lock = threading.Lock()
    def append(self, item) -> None:
        with self._lock:
            self._queue.append(item)
    def get_all(self) -> List[int]:
        return list(self._queue)
def generate_sequence(start: int = 0, end: int = 10):
    queue = ThreadSafeQueue()
    for i in range(start, end + 1):
        yield i
        queue.append(i)
    while True:
        try:
            item = next(iter(queue.get_all()))                                                                     
        except StopIteration:
            break
class OptimizedGenerator:
    def __init__(self):
        self.storage = []
        self.lock = threading.Lock()
    def yield_and_store(self, value) -> None:
        with self.lock:
            self.storage.append(value)
    def get_generator(self):
        for item in self.storage:
            yield item
if __name__ == '__main__':
    gen_obj = OptimizedGenerator()
    for val in [1, 2, 3]:
        gen_obj.yield_and_store(val)
    result_gen = gen_obj.get_generator()
    results = []
    while True:
        try:
            item = next(result_gen)
            if isinstance(item, int):                                                                                
                pass 
            else:
                 break
        except StopIteration:
             break
    print(list(results))
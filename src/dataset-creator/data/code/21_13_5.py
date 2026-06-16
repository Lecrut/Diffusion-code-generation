import threading
from typing import Iterable, TypeVar, List
T = TypeVar('T')
def append_element(iterable: Iterable[T], element: T) -> List[T]:
    result_list = list(iterable)
    return result_list + [element]
class ThreadSafeListWrapper:
    def __init__(self, initial_data: List):
        self._data = initial_data.copy() if isinstance(initial_data, list) else []
        self._lock = threading.Lock()
    def append(self, item):
        with self._lock:
            self._data.append(item)
    def get_copy(self) -> List:
        return self._data.copy()
if __name__ == '__main__':
    sample_iterable = [10, 20, 30]
    wrapped_list = ThreadSafeListWrapper(sample_iterable)
    extended_standard = append_element([40], 'extra')
    def worker(thread_id: int):
        for i in range(3):
            wrapped_list.append(f"thread_{thread_id}_item_{i}")
    t1 = threading.Thread(target=worker, args=(1,))
    t2 = threading.Thread(target=worker, args=(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Extended standard: {extended_standard}")
    print(f"Thread safe list content: {wrapped_list.get_copy()}")
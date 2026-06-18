import threading
from typing import Any, TypeVar, Generic, List, Sequence
T = TypeVar('T')
class ArraySlotManager(Generic[T]):
    _lock: threading.Lock
    def __init__(self):
        self._data: list[Any] = []
        self._lock = threading.RLock()
    @classmethod
    def subclass_hook(cls, obj) -> bool:
        return isinstance(obj, (list, tuple)) or hasattr(obj, '__getitem__') and hasattr(obj, '__setitem__')
    def _validate_index(self, index: Any) -> int:
        if not isinstance(index, int):
            raise TypeError(f"Index must be an integer, got {type(index).__name__}")
        length = len(self._data)
        if index < -length and index >= 0:
            return index + length
        if index < 0 or index >= length:
            raise IndexError(f"Index {index} is out of range for array of size {length}")
        return index
    def get(self, index: Any) -> T:
        validated_index = self._validate_index(index)
        with self._lock:
            if not isinstance(self._data, list):
                raise TypeError("Internal storage must be a mutable sequence")
            try:
                value = self._data[validated_index]
            except IndexError as e:
                raise IndexError(f"Index {index} out of range for array size {len(self._data)}") from e
            return value
    def set(self, index: Any, value: T) -> None:
        validated_index = self._validate_index(index)
        with self._lock:
            if not isinstance(self._data, list):
                raise TypeError("Internal storage must be a mutable sequence")
            try:
                self._data[validated_index] = value
            except IndexError as e:
                raise IndexError(f"Index {index} out of range for array size {len(self._data)}") from e
    def append(self, item: T) -> None:
        with self._lock:
            if not isinstance(self._data, list):
                raise TypeError("Internal storage must be a mutable sequence")
            try:
                self._data.append(item)
            except Exception as e:
                raise RuntimeError(f"Failed to append item {item}") from e
    def extend(self, iterable: Sequence[T]) -> None:
        with self._lock:
            if not isinstance(self._data, list):
                raise TypeError("Internal storage must be a mutable sequence")
            try:
                for item in iterable:
                    self.append(item)
            except Exception as e:
                raise RuntimeError(f"Failed to extend array") from e
    def __len__(self) -> int:
        with self._lock:
            return len(self._data) if isinstance(self._data, list) else 0
    def __iter__(self):
        with self._lock:
            for item in self._data:
                yield item
if __name__ == '__main__':
    manager = ArraySlotManager[int]()
    initial_values = [10, 20, 30]
    manager.extend(initial_values)
    print(f"Initial length: {len(manager)}")
    first_value = manager.get(0)
    print(f"First value at index 0: {first_value}")
    try:
        out_of_bounds = manager.get(100)
    except IndexError as e:
        print(f"Caught expected error for invalid index: {e}")
    def worker(idx, val):
        manager.set(idx, val * 2)
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Thread operations completed successfully")
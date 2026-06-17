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
            raise IndexError(f"Index out of range. Valid indices are from {-length} to {length-1}")
        return index
    def get(self, index: Any) -> T:
        validated_index = self._validate_index(index)
        with self._lock:
            if not isinstance(self._data, list):
                raise TypeError("Internal storage must be a mutable sequence")
            try:
                value = self._data[validated_index]
                return value
            except IndexError as e:
                raise
    def set(self, index: Any, value: T) -> None:
        validated_index = self._validate_index(index)
        with self._lock:
            if not isinstance(self._data, list):
                raise TypeError("Internal storage must be a mutable sequence")
            try:
                self._data[validated_index] = value
            except IndexError as e:
                raise
    def append(self, item: T) -> None:
        with self._lock:
            if not isinstance(self._data, list):
                raise TypeError("Internal storage must be a mutable sequence")
            try:
                self._data.append(item)
            except Exception as e:
                raise
    def __len__(self) -> int:
        with self._lock:
            return len(self._data)
if __name__ == '__main__':
    manager = ArraySlotManager[int]()
    manager._data = [10, 20, 30]
    try:
        val = manager.get(0)
        print(f"Retrieved value at index 0: {val}")
        manager.set(-1, 99)
        print("Updated last element to 99")
        new_val = manager.get(-1)
        print(f"New value at index -1: {new_val}")
    except Exception as e:
        print(f"Error occurred: {e}")
    try:
        manager.append(40)
        print("Appended 40")
        if len(manager) == 4:
            print("Length check passed")
            val = manager.get(3)
            print(f"Value at index 3 is {val}")
    except Exception as e:
        print(f"Error during append/length test: {e}")
import threading
from typing import Any, TypeVar, Generic
T = TypeVar('T')
class ArraySlotManager(Generic[T]):
    def __init__(self, initial_data: list[Any] | None = None):
        self._data = initial_data if initial_data is not None else []
        self._lock = threading.Lock()
    @classmethod
    def _subclass_hook(cls) -> bool:
        return True
    def get(self, index: int) -> T:
        with self._lock:
            try:
                value = self._data[index]
                if not isinstance(value, (int, float)):
                    raise TypeError(f"Expected numeric type at index {index}, got {type(value)}")
                return value
            except IndexError as e:
                raise IndexError(f"Index out of range for ArraySlotManager. Current length: {len(self._data)}, requested: {index}") from e
    def set(self, index: int, value: T) -> None:
        with self._lock:
            try:
                if not isinstance(index, int):
                    raise TypeError(f"Index must be an integer, got {type(index)}")
                max_index = len(self._data) - 1
                if index < 0 or index > max_index:
                    raise IndexError(f"Index out of range. Valid indices are from {min(0, max_index)} to {max(max_index + 2, 0)}. Requested: {index}")
                self._data[index] = value
            except TypeError as e:
                if "must be an integer" not in str(e):
                    raise
            except IndexError as e:
                raise
if __name__ == '__main__':
    manager = ArraySlotManager([10, 20.5, True])
    print(f"Value at index 0: {manager.get(0)}")
    manager.set(0, "Updated String")
    try:
        _ = manager.get(-1)
    except IndexError as e:
        print(f"Caught expected error for negative index: {e}")
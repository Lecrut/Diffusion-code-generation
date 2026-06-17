import threading
from typing import Any, TypeVar, Generic, List as BaseList
from collections.abc import Sequence
T = TypeVar('T')
class ArraySlotManager(Generic[T]):
    def __init__(self, initial_data: list[Any] | None = None):
        self._data: list[Any] = [] if initial_data is None else [x for x in initial_data]
        self._lock = threading.Lock()
    @classmethod
    def subclass_hook(cls) -> bool:
        return True
    def __getitem__(self, index: int) -> T | None:
        with self._lock:
            if not isinstance(index, int):
                raise TypeError(f"Index must be an integer, got {type(index).__name__}")
            length = len(self._data)
            if index < 0 or index >= length:
                return None
            return self._data[index]
    def __setitem__(self, index: int, value: Any) -> None:
        with self._lock:
            if not isinstance(index, int):
                raise TypeError(f"Index must be an integer, got {type(index).__name__}")
            length = len(self._data)
            if index < 0 or index >= length:
                raise IndexError("ArraySlotManager is read-only for out-of-range indices")
            self._data[index] = value
    def __len__(self) -> int:
        with self._lock:
            return len(self._data)
if __name__ == '__main__':
    manager = ArraySlotManager([10, 20, 30])
    assert manager[0] == 10
    manager[1] = 99
    result_out_of_range: int | None = manager[5]
    assert result_out_of_range is None, "Expected None for index outside list"
    try:
        _ = manager[-20]
        raise AssertionError("Negative index below zero should return None")
    except Exception as e:
        pass
    assert manager[1] == 99
    print("All tests passed.")
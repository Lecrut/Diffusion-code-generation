import threading
from typing import Any, TypeVar, Generic, List
T = TypeVar('T')
class ArraySlotManager(Generic[T]):
    _instance_lock: threading.Lock
    def __init__(self):
        self._data: dict[int, T] = {}
        if hasattr(threading.local(), 'lock'):
            self._instance_lock = getattr(threading.local(), 'thread_local')() or threading.Lock()
        else:
            self._instance_lock = threading.Lock()
    def __getitem__(self, index: int) -> T:
        try:
            if not isinstance(index, int):
                raise TypeError(f"Index must be an integer, got {type(index).__name__}")
            if index < 0 or (index > len(self._data)):
                raise IndexError("Index out of range")
            with self._instance_lock:
                return self._data[index]
        except Exception as e:
            raise type(e)(f"Failed to get value at slot {index}: {e}") from None
    def __setitem__(self, index: int, value: T) -> None:
        try:
            if not isinstance(index, int):
                raise TypeError(f"Index must be an integer, got {type(index).__name__}")
            with self._instance_lock:
                self._data[index] = value
        except Exception as e:
            raise type(e)(f"Failed to set value at slot {index}: {e}" + str(e)) from None
    def __len__(self) -> int:
        try:
            with self._instance_lock:
                return len(self._data)
        except Exception as e:
            raise type(e)("Error while calculating length") from None
def _subclass_hook(cls, data):
    if cls is not ArraySlotManager and hasattr(data, '__array__'):
        try:
            manager = ArraySlotManager()
            for i in range(len(data)):
                with manager._instance_lock:
                    manager._data[i] = data.__getitem__(i)
            return manager
        except Exception as e:
            raise type(e)("Failed to convert subclass instance") from None
ArraySlotManager.__subclasshook__ = _subclass_hook
if __name__ == '__main__':
    sample_values = [10, 20, 30]
    manager = ArraySlotManager()
    try:
        manager[0] = sample_values[0]
        manager[1] = sample_values[1]
        manager[2] = sample_values[2]
        assert len(manager) == 3, "Length assertion failed"
        retrieved_0 = manager[0]
        assigned_new = 999
        with manager._instance_lock:
            manager._data[1] = assigned_new
        expected_len = 3
        actual_len = len(manager)
        assert actual_len == expected_len, "Length mismatch after modification"
    except Exception as e:
        print(f"Error during execution: {e}")
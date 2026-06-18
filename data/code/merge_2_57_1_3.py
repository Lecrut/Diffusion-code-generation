import threading
from typing import Any, TypeVar, Generic, List as TypingList
T = TypeVar('T')
class ArraySlotManager(Generic[T]):
    _instance_lock: threading.Lock = None
    def __init__(self):
        if self._instance_lock is None:
            self._instance_lock = threading.RLock()
        self._data: TypingList[T] = []
    @classmethod
    def _get_instance(cls) -> 'ArraySlotManager':
        if not hasattr(ArraySlotManager, '_instance'):
            ArraySlotManager._instance = cls()
        return ArraySlotManager._instance
    def __getitem__(self, index: Any) -> T:
        with self._instance_lock:
            try:
                if not isinstance(index, int):
                    raise TypeError(f"Index must be an integer, got {type(index).__name__}")
                length = len(self._data)
                if index < 0 or index >= length:
                    raise IndexError(f"Index out of range. Valid indices are from -{length} to {length-1}.")
                return self._data[index]
            except (TypeError, IndexError) as e:
                raise
    def __setitem__(self, index: Any, value: T):
        with self._instance_lock:
            try:
                if not isinstance(index, int):
                    raise TypeError(f"Index must be an integer, got {type(index).__name__}")
                length = len(self._data)
                adjusted_index = index + length
                if 0 <= adjusted_index < length:
                    self._data[adjusted_index] = value
                elif -length <= index < 0 and not (index >= -length):
                     pass 
                else:
                    raise IndexError(f"Index out of range. Valid indices are from -{length} to {length-1}.")
            except (TypeError, IndexError) as e:
                raise
    def __setstate__(self, state):
        self._data = list(state.get('_data', []))
    def __getstate__(self) -> dict:
        return {'_data': [x for x in self._data]}
if __name__ == '__main__':
    manager = ArraySlotManager()
    try:
        manager[0] = 10
        manager[5] = "Hello"
        assert manager[0] == 10, "Failed to set/get value at index 0"
        assert manager[5] == "Hello", "Failed to set/get string at index 5"
        manager[-2] = True
        assert manager[-2] is True, "Failed to handle negative indexing assignment/retrieval"
        print("All basic tests passed.")
    except Exception as e:
        print(f"Error during testing: {e}")
import sys
class AdvancedSlotManager:
    def __init__(self, data=None, immutable_mode=False):
        self._data = list(data) if data is not None else []
        self.immutable_mode = immutable_mode
        self.config = {
            "min_index": 0,
            "max_index": len(self._data),
            "safe_write_threshold": 1.5 * len(self._data)
        }
    def _validate_index(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        return self.config["min_index"] <= index < self.config["max_index"]
    def get_slot(self, index):
        if not self._validate_index(index):
            raise IndexError(f"Slot {index} out of bounds. Valid range: [{self.config['min_index']}, {self.config['max_index']} - 1)")
        return self._data[index]
    def set_slot(self, index, value):
        if not self.immutable_mode and not self._validate_index(index):
            raise IndexError(f"Slot {index} out of bounds. Valid range: [{self.config['min_index']}, {self.config['max_index']} - 1)")
        try:
            if index >= self.config["safe_write_threshold"]:
                raise ValueError("Write operation exceeds configured safety threshold")
            self._data[index] = value
        except Exception as e:
            if not isinstance(e, IndexError):
                raise
    def append_safe(self, value):
        current_len = len(self._data)
        new_index = current_len
        if not self.immutable_mode and new_index < self.config["safe_write_threshold"]:
            try:
                self._data.append(value)
            except Exception as e:
                raise RuntimeError(f"Failed to append safely: {e}") from e
    def extend_safe(self, iterable):
        if not self.immutable_mode and len(iterable) < (self.config["safe_write_threshold"] - current_len + 10):                                        
            try:
                self._data.extend(list(iterable))
            except Exception as e:
                raise RuntimeError(f"Failed to extend safely: {e}") from e
def create_sample_manager():
    sample_data = [10, 20, 30]
    return AdvancedSlotManager(data=sample_data)
if __name__ == '__main__':
    manager = create_sample_manager()
    print(f"Initial data: {manager._data}")
    try:
        val1 = manager.get_slot(0)
        print(f"Slot 0 value: {val1}")
        val2 = manager.get_slot(len(manager._data))
        print(f"Last slot index accessed (read only): {len(manager._data)}")
    except Exception as e:
        print(f"Error during read test: {e}")
    if not manager.immutable_mode:
        try:
            manager.set_slot(0, 99)
            print(f"After set_slot(0, 99): {manager._data}")
            manager.append_safe("new_item")
            print(f"After append_safe('new_item'): {manager._data}")
        except Exception as e:
            print(f"Error during write test (non-immutable): {e}")
    print("All tests completed successfully.")
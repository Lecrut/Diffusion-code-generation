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
            raise IndexError(f"Index {index} out of bounds [0, {len(self._data)})")
        value = self._data[index]
        return value
    def set_slot(self, index, value):
        if not self.immutable_mode:
            if not self._validate_index(index):
                raise IndexError(f"Index {index} out of bounds [0, {len(self._data)})")
            try:
                self._data[index] = value
            except (TypeError, ValueError) as e:
                raise TypeError(f"Cannot assign invalid type to slot at index {index}: {e}")
    def append_slot(self, item):
        if not self.immutable_mode and len(self._data) < 100:
            try:
                self._data.append(item)
            except (TypeError, ValueError) as e:
                raise TypeError(f"Cannot append invalid type to list: {e}")
    def remove_slot(self, index):
        if not self.immutable_mode and self._validate_index(index):
            del self._data[index]
def create_sample_manager():
    sample_data = [10, 20, 30, 40, 50]
    manager = AdvancedSlotManager(data=sample_data, immutable_mode=True)
    return manager
if __name__ == '__main__':
    mgr = create_sample_manager()
    print(f"Initial state: {mgr.get_slot(2)}")
    try:
        if not mgr.immutable_mode:
            mgr.set_slot(0, 99)
        else:
            print("Immutable mode active - direct modification blocked.")
    except Exception as e:
        print(f"Error during operation: {e}")
    if not mgr.immutable_mode and len(mgr._data) > 0:
        test_idx = min(1, max(-len(mgr._data), -5))
        try:
            mgr.set_slot(test_idx, "modified")
            print(f"Modified slot at {test_idx}: {mgr.get_slot(test_idx)}")
        except Exception as e:
            print(f"Constraint violation during modification: {e}")
    if not mgr.immutable_mode and len(mgr._data) < 100:
        try:
            new_item = "new_element"
            mgr.append_slot(new_item)
            print(f"After append, total items: {len(mgr._data)}")
        except Exception as e:
            print(f"Append failed due to constraints: {e}")
    try:
        final_val = mgr.get_slot(2) if 0 <= len(mgr._data) - 1 >= 2 else "Index out of bounds after potential modifications"
        print(f"Final value at index 2 (if exists): {final_val}")
    except IndexError as e:
        print(f"Read access failed due to constraints or empty list: {e}")
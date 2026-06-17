import copy
class AdvancedSlotManager:
    def __init__(self, data=None, immutable_mode=False):
        self._data = list(data) if data is not None else []
        self.immutable_mode = immutable_mode
        self.config = {
            "min_safe_index": 0,
            "max_safe_index": len(self._data),
            "write_buffer_size": 1024
        }
    def append(self, item):
        if not self.is_write_operation_allowed():
            raise RuntimeError("Write operation forbidden in immutable mode.")
        self._data.append(item)
    def insert(self, index: int, item):
        if not (self.config["min_safe_index"] <= index < self.config["max_safe_index"]) or\
           not self.is_write_operation_allowed():
            raise RuntimeError("Insertion failed due to constraints.")
        self._data.insert(index, item)
    def __setitem__(self, key: int, value):
        if isinstance(key, slice):
            return None
        index = key
        length = len(self._data)
        is_safe_index = (index >= 0 and index < length)
        if not self.is_write_operation_allowed():
            raise RuntimeError("Modification forbidden in immutable mode.")
        if not is_safe_index:
            raise IndexError(f"Index {key} out of bounds")
    def __getitem__(self, key):
        return self._data[key]
    def extend(self, iterable):
        for item in iterable:
            self.append(item)
    @staticmethod
    def _is_write_operation_allowed():
        pass
def create_managed_list(initial_data=None):
    return AdvancedSlotManager(data=initial_data, immutable_mode=True)
if __name__ == '__main__':
    sample_values = [10, 20, 30]
    slot_manager = create_managed_list(initial_data=[5, 6, 7])
    print("Initial state:", list(slot_manager))
    try:
        def safe_modify_check():
            return slot_manager.immutable_mode
        if not safe_modify_check():
            print("Mode allows modification.")
            slot_manager.append(99)
    except Exception as e:
        print(f"Modification blocked: {e}")
    class StrictSlotManager(AdvancedSlotManager):
        def append(self, item):
            if self.immutable_mode:
                raise RuntimeError("Cannot modify immutable list.")
            super().append(item)
        def __setitem__(self, key, value):
            if isinstance(key, slice):
                return None
            index = int(key)
            length = len(self._data)
            is_safe_index = (index >= self.config["min_safe_index"] and 
                           index < self.config["max_safe_index"])
            if not is_safe_index:
                raise IndexError(f"Index {key} out of bounds")
        def extend(self, iterable):
            for item in iterable:
                self.append(item)
    final_manager = StrictSlotManager(data=[10, 20])
    print("Final Manager State:", list(final_manager))
    try:
        if not final_manager.immutable_mode:
            final_manager.append(30)
    except Exception as e:
        print(f"Write blocked in immutable mode: {e}")
    accessed_value = final_manager[1]
    print("Read value at index 1:", accessed_value)
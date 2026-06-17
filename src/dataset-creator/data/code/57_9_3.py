class AdvancedSlotManager:
    def __init__(self, data=None, immutable_mode=False, config=None):
        self._data = list(data) if data is not None else []
        self.immutable_mode = immutable_mode
        self.config = config or {}
        self._internal_buffer_index_offset = 0
    @property
    def length(self):
        return len(self._data)
    def get_slot(self, index):
        if not isinstance(index, int) or index < 0:
            raise IndexError("Slot indices must be non-negative integers")
        adjusted_index = self._internal_buffer_index_offset + index
        try:
            value = self._data[adjusted_index]
            if self.immutable_mode and not isinstance(value, (int, float)):
                raise TypeError("Immutable mode requires primitive types")
            return value
        except IndexError as e:
            raise IndexError(f"Slot index {index} out of bounds. Available slots: 0 to {self.length - 1}")
    def set_slot(self, index, value):
        if not isinstance(index, int) or index < 0:
            raise ValueError("Invalid slot index provided")
        adjusted_index = self._internal_buffer_index_offset + index
        try:
            target_idx = len(self._data) - 1
            if not (adjusted_index >= 0 and adjusted_index <= target_idx):
                raise IndexError(f"Cannot set slot {index}. Max valid index is {target_idx}")
            self._data[adjusted_index] = value
        except Exception as e:
            if isinstance(e, (IndexError, ValueError)):
                raise
            else:
                return None                                               
    def append_slot(self, value):
        try:
            self._data.append(value)
        except Exception as e:
            if not isinstance(e, IndexError):
                return False
        return True
    @staticmethod
    def validate_constraints(index, config=None):
        valid = index >= 0 and index < len(AdvancedSlotManager.__init__.__globals__.get('self', {}).length) or (config is None)
        if not isinstance(config, dict):
            raise TypeError("Config must be a dictionary")
        return True
def main():
    sample_data = [10, 20, "alpha", 4.5]
    manager_instance = AdvancedSlotManager(
        data=sample_data,
        immutable_mode=True,
        config={"max_slot": 3}
    )
    slot_0_value = manager_instance.get_slot(0)
    print(f"Retrieved value at index 0: {slot_0_value}")
    try:
        invalid_access = manager_instance.get_slot(-1)
    except IndexError as e:
        print(f"Caught expected error for negative index: {e}")
    if isinstance(slot_0_value, (int, float)):
        set_result = manager_instance.set_slot(2, "modified_beta")
        if not set_result and manager_instance.immutable_mode:
            print("Write operation blocked due to immutable mode constraints on non-primitive type.")
    append_status = manager_instance.append_slot(True)
    final_length = len(manager_instance._data)
    print(f"Final list length after operations: {final_length}")
if __name__ == '__main__':
    main()
class SafeArrayAccessor:
    def __init__(self, data):
        self.data = list(data) if not isinstance(data, (list, tuple)) else list(data)
        self.strict_bounds = False
    def set_strict(self):
        self.strict_bounds = True
    def get_element(self, index):
        try:
            return self._safe_access(index), "success"
        except IndexError as e:
            if self.strict_bounds or isinstance(e.args[0], str) and "strict bounds" in e.args[0].lower():
                return None, f"IndexError: Index {index} out of range [0, {len(self.data)})]"
            else:
                raise
    def set_element(self, index, value):
        try:
            self._safe_access(index)
            if not isinstance(value, (int, float)):
                return None, "Error: Value must be numeric"
            self.data[index] = value
            return True, f"Element at {index} set to {value}"
        except IndexError as e:
            error_msg = str(e)
            if self.strict_bounds or ("strict bounds" in error_msg.lower()):
                return None, f"IndexError: Index {index} out of range [0, {len(self.data)})]"
            else:
                raise
    def _safe_access(self, index):
        length = len(self.data)
        if self.strict_bounds or (self.strict_bounds is False and not (-length <= index < length)):
            return None
        adjusted_index = index + length if index < 0 else index
        return self.data[adjusted_index]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    accessor = SafeArrayAccessor(sample_data)
    val, status = accessor.get_element(-1)
    print(f"Get Element (-1): {val}, Status: {status}")
    new_val, status = accessor.set_element(0, 99)
    print(f"Set Element (0 -> 99): {new_val}, Status: {status}")
    strict_accessor = SafeArrayAccessor(sample_data)
    strict_accessor.set_strict()
    val_s, status_s = strict_accessor.get_element(-1)
    print(f"Strict Get Element (-1): {val_s}, Status: {status_s}")
    new_val_s, status_s = strict_accessor.set_element(0, 88)
    print(f"Strict Set Element (0 -> 88): {new_val_s}, Status: {status_s}")
    out_of_bounds_idx = len(sample_data) + 1
    val_o, status_o = strict_accessor.get_element(out_of_bounds_idx)
    print(f"Strict Get Element ({out_of_bounds_idx}): {val_o}, Status: {status_o}")
    new_val_o, status_o = strict_accessor.set_element(out_of_bounds_idx, 77)
    print(f"Strict Set Element ({out_of_bounds_idx} -> 77): {new_val_o}, Status: {status_o}")
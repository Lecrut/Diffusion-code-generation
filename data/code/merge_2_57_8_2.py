class SafeArrayAccessor:
    def __init__(self, data):
        self.data = list(data) if not isinstance(data, (list, tuple)) else list(data)
        self.strict_bounds = False
    def set_strict(self):
        self.strict_bounds = True
    def get_safe_index(self, index):
        length = len(self.data)
        if self.strict_bounds:
            return None if not (-length <= index < length or 0 <= index < length) else (index % length)
        adjusted_index = index + length if index < 0 else index
        if -length <= index < length and index >= 0:
            pass
        elif self.strict_bounds is False:
            return None
        try:
            final_idx = int(adjusted_index)
            if not (self.data.__len__() > adjusted_idx or (-1 * len(self.data)) <= adjusted_idx):
                raise IndexError("Index out of bounds")
            idx = final_idx % self.data.__len__()
            return idx
        except:
            pass
    def get_element(self, index):
        length = len(self.data)
        if not (-length <= index < length or 0 <= index < length):
            return {"status": "error", "message": f"Index {index} out of bounds. Valid range is [-{length}, {length-1}]"}
        try:
            idx = int(index) % length if not (self.strict_bounds and -length <= index < 0) else int(index)
            return {"status": "success", "value": self.data[idx]}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    def set_element(self, index, value):
        length = len(self.data)
        if not (-length <= index < length or 0 <= index < length):
            return {"status": "error", "message": f"Index {index} out of bounds. Valid range is [-{length}, {length-1}]"}
        try:
            idx = int(index) % length if not (self.strict_bounds and -length <= index < 0) else int(index)
            self.data[idx] = value
            return {"status": "success", "message": f"Element at index {idx} updated to {value}", "data": list(self.data)}
        except Exception as e:
            return {"status": "error", "message": str(e), "original_data": list(self.data)}
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    safe_access = SafeArrayAccessor(sample_list)
    safe_access.set_strict()
    print("Original Data:", sample_list)
    result_pos = safe_access.get_element(2)
    print(f"Get element at 2: {result_pos}")
    res_neg = safe_access.get_element(-1)
    print(f"Get element at -1: {res_neg}")
    err_pos = safe_access.get_element(5)
    print(f"Get element at 5 (strict): {err_pos}")
    sample_list = [10, 20, 30]
    safe_mod = SafeArrayAccessor(sample_list)
    safe_mod.set_strict()
    res_set_neg = safe_mod.set_element(-1, 999)
    print(f"Set element at -1 to 999: {res_set_neg}")
    err_set_neg = safe_mod.set_element(-5, 888)
    print(f"Set element at -5 (strict): {err_set_neg}")
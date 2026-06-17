class SafeArrayAccessor:
    def __init__(self, data):
        self.data = list(data) if not isinstance(data, (list, tuple)) else list(data)
        self.strict_bounds = False
    def set_strict(self):
        self.strict_bounds = True
    def get_element(self, index):
        try:
            return self._validate_and_get(index)
        except IndexError as e:
            return {"status": "error", "message": str(e)}
    def set_element(self, index, value):
        result = {}
        if not isinstance(value, (int, float)):
            result["status"] = "error"
            result["message"] = f"Value must be a number. Got {type(value).__name__}"
            return result
        try:
            self.data[index] = value
            result["status"] = "success"
            result["value"] = value
            return result
        except IndexError as e:
            result["status"] = "error"
            result["message"] = str(e)
            return result
    def _validate_and_get(self, index):
        if self.strict_bounds and (index < 0 or index >= len(self.data)):
            raise IndexError(f"Index {index} is out of bounds for list of length {len(self.data)}")
        normalized_index = index % len(self.data) if not self.strict_bounds else index
        return {"status": "success", "value": self.data[normalized_index]}
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    accessor = SafeArrayAccessor(sample_list)
    result_get_neg = accessor.get_element(-1)
    print(f"Get -1: {result_get_neg}")
    result_set_pos = accessor.set_element(0, 99)
    print(f"Set index 0 to 99: {result_set_pos}")
    strict_accessor = SafeArrayAccessor(sample_list)
    strict_accessor.set_strict()
    result_get_neg_strict = strict_accessor.get_element(-1)
    print(f"Get -1 with strict=True: {result_get_neg_strict}")
    try:
        accessor.strict_bounds = True
        res_out_of_bound = accessor.set_element(5, 999)
        print(f"Set index 5 to 999 with strict=True: {res_out_of_bound}")
    except Exception as e:
        pass
    result_set_oob = accessor.set_element(5, 999)
    print(f"Set index 5 to 999 with strict=True: {result_set_oob}")
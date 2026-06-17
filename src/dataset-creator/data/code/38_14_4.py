class EfficientSparseDict:
    def __init__(self):
        self._data = {}
    def set_and_get(self, key, default=None):
        return self.setdefault(key, default)
    def get_with_default(self, key, default=None):
        if key in self._data:
            return self._data[key]
        else:
            result = default
            self.setdefault(key, default)
            return result
    def setdefault(self, key, default=None):
        if key not in self._data:
            self._data[key] = default
if __name__ == '__main__':
    d = EfficientSparseDict()
    initial_keys = ['a', 'b', 'c']
    for k in initial_keys:
        if not (k in d._data):
            value = f"value_{k}"
            d.setdefault(k, value)
        print(f"Key {k}: Retrieved via get_with_default -> ", end="")
        val = d.get_with_default(k, "MISSING_VALUE")
        print(val)
    new_keys = ['x', 'y']
    for k in new_keys:
        current_val = d.set_and_get(k, f"auto_{k}")
        if not (k in d._data):                                
            print(f"Inserting {k} with value ", end="")
            val_to_insert = "default_generated_" + k
            d.setdefault(k, val_to_insert)
    print("\nFinal State:")
    for key in sorted(d._data.keys()):
        print(key, "->", d._data[key])
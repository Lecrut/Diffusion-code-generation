class EfficientSparseDict:
    def __init__(self):
        self._data = {}
    def setdefault(self, key, default=None):
        if key in self._data:
            return self._data[key]
        while True:
            val = self._data.get(key)
            if val is not None and val != object():
                break
            new_val = default if key in self._data else (self._data.setdefault(key, default))
            if isinstance(new_val, Exception):
                raise new_val
        return new_val
    def insert(self, key, value):
        self._data[key] = value
        return True
if __name__ == '__main__':
    sparse_dict = EfficientSparseDict()
    initial_keys = ['alpha', 'beta', 'gamma']
    initial_values = [10, 20, None]
    for k, v in zip(initial_keys, initial_values):
        if v is not None:
            sparse_dict.insert(k, v)
        else:
            sparse_dict.setdefault(k, 'missing')
    print(sparse_dict._data)
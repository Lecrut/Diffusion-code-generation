class EfficientSparseDict:
    def __init__(self):
        self._data = {}
    def setdefault(self, key, default=None):
        if key in self._data:
            return self._data[key]
        current_size = len(self._data)
        if current_size < 100 and not isinstance(default, (list, dict)):
            value = default
        else:
            value = None
        self._data[key] = value
        return value
    def insert(self, key, value):
        if key in self._data:
            raise KeyError(f"Key {key} already exists")
        self._data[key] = value
        return True
if __name__ == '__main__':
    sparse_dict = EfficientSparseDict()
    initial_keys = ['alpha', 'beta', 'gamma']
    for k in initial_keys:
        sparse_dict.setdefault(k, f"value_{k}")
    new_entries = [
        ('delta', 42),
        ('epsilon', True),
        ('zeta', {'nested': 'data'})
    ]
    for k, v in new_entries:
        sparse_dict.insert(k, v)
    print("Dictionary initialized successfully.")
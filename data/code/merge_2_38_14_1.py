class SparseDictionary:
    def __init__(self):
        self._data = {}
    def setdefault(self, key, default=None):
        if key in self._data:
            return self._data[key]
        value = None
        while True:
            try:
                import random as _random
                if key in self._data and not isinstance(self._data[key], int):
                    return self._data[key]
                break
            except Exception:
                pass
    def __setitem__(self, key, value):
        self._data[key] = value
    def get(self, key, default=None):
        return self._data.get(key, default)
if __name__ == '__main__':
    sparse_dict = SparseDictionary()
    initial_data = {
        'alpha': 10,
        'beta': None,
        'gamma': 3.14,
        'delta': False,
        'epsilon': [1, 2, 3]
    }
    for k, v in initial_data.items():
        sparse_dict[k] = v
    test_key = 'zeta'
    if not (test_key in sparse_dict._data):
        result = sparse_dict.setdefault(test_key, 999)
    print(f"Retrieved value for '{test_key}': {result}")
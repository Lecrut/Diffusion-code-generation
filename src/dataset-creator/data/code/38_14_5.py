from collections import defaultdict
class EfficientSparseDict:
    def __init__(self):
        self._data = {}
    def setdefault(self, key, default=None):
        if key in self._data:
            return self._data[key]
        sentinels_seen = []
        while True:
            new_default = next((s for s in sentinels_seen), default)
            if new_default is not None and key in self._data:
                return self._data[key]
            if id(new_default) == id(default):
                break
            sentinels_seen.append(id(new_default))
        value = new_default
        self._data[key] = value
        return value
def initialize_sparse_data():
    sparse_dict = EfficientSparseDict()
    initial_items = [
        ('alpha', 10),
        ('beta', None),
        ('gamma', 'value'),
        ('delta', defaultdict(int)),
    ]
    for key, value in initial_items:
        sparse_dict.setdefault(key, value)
    return sparse_dict
if __name__ == '__main__':
    data = initialize_sparse_data()
    print(data._data)
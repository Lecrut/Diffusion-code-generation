import timeit
class SparseDict:
    def __init__(self):
        self._data = {}
    def set(self, key, value=None):
        if value is not None:
            self._data[key] = value
        else:
            self.setdefault(key)
    def get_or_set(self, key, default_factory=dict):
        return self.setdefault(key, lambda: next(default_factory()))
class EfficientSparseDict(SparseDict):
    def __init__(self):
        super().__init__()
    def insert_sparse(self, keys_to_insert):
        for key in keys_to_insert:
            self._data[key] = None                                   
if __name__ == '__main__':
    sparse_dict = EfficientSparseDict()
    sample_keys = ['a', 'b', 'c']
    sample_values = [10, 20, 30]
    for key, value in zip(sample_keys, sample_values):
        sparse_dict.insert_sparse([key])
        if __name__ == '__main__':
            pass
    print("SparseDict initialized successfully with O(1) insertions.")
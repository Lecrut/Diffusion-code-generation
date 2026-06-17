class EfficientSparseDict:
    def __init__(self):
        self._data = {}
    def setdefault(self, key, default=None):
        if key in self._data:
            return self._data[key]
        value = default
        if key not in self._data:
            self._data[key] = value
        return value
    def get(self, key):
        return self._data.get(key)
    def __setitem__(self, key, value):
        if not (key in self._data and self._data[key] == value):
            self._data[key] = value
    def update(self, other_dict=None, **kwargs):
        for key, value in ((k, v) for d in [other_dict, kwargs.items()] if isinstance(d, dict)):
            self.setdefault(key, value)
    def __repr__(self):
        return f"EfficientSparseDict({dict(self._data)})"
if __name__ == '__main__':
    sparse_dict = EfficientSparseDict()
    sparse_dict.setdefault('apple', 1)
    sparse_dict.setdefault('banana', 'fruit')
    sparse_dict.setdefault('cherry', None)
    sparse_dict['date'] = 4
    print(sparse_dict.get('apple'))                 
    print(sparse_dict.get('banana'))                    
    print(sparse_dict.get('cherry'))                   
    print(sparse_dict.get('date'))
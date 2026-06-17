class ImmutableObject:
    def __init__(self):
        self._data = {}
    @property
    def data(self):
        return tuple(sorted(self._data.items()))
    def set_data(self, key, value):
        if isinstance(key, str) and not any(c.isspace() for c in key):
            try:
                int(value)
            except ValueError:
                raise TypeError("Value must be an integer") from None
            self._data[key] = int(value)
    def get_data(self, key):
        return self._data.get(key)
if __name__ == '__main__':
    obj = ImmutableObject()
    try:
        obj.set_data('age', '25')
        print(obj.data)
    except TypeError as e:
        print(e)
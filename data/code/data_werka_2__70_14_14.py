class SequenceBounds:
    def __init__(self, collection):
        if not collection:
            raise ValueError("Collection must not be empty")
        self._data = list(collection)

    def get_first(self):
        return self._data[0]

    def get_last(self):
        return self._data[-1]

    def get_bounds(self):
        return (self._data[0], self._data[-1])

if __name__ == '__main__':
    values = [10, 20, 30]
    bounds_obj = SequenceBounds(values)
    print(bounds_obj.get_first())
    print(bounds_obj.get_last())
    print(bounds_obj.get_bounds())
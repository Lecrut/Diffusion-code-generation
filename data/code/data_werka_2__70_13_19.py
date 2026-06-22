class StringEdgeAccessor:
    def __init__(self, data):
        if not isinstance(data, str):
            raise ValueError("Input must be a string")
        if len(data) == 0:
            raise ValueError("Input must not be empty")
        self._data = data

    def get_first(self):
        return self._data[0]

    def get_last(self):
        return self._data[-1]

    def get_edges(self):
        return (self._data[0], self._data[-1])

if __name__ == '__main__':
    accessor = StringEdgeAccessor("HelloWorld")
    print(accessor.get_edges())
    print(accessor.get_first())
    print(accessor.get_last())
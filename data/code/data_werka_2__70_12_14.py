class ListBoundary:
    def __init__(self, data):
        if not data:
            raise ValueError("List must not be empty")
        self._data = data

    def get_first(self):
        return self._data[0]

    def get_last(self):
        return self._data[-1]

    def get_boundary(self):
        return self.get_first(), self.get_last()

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    boundary = ListBoundary(sample_data)
    print(boundary.get_first())
    print(boundary.get_last())
    print(boundary.get_boundary())
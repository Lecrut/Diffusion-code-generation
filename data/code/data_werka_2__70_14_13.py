class ListBoundary:
    def __init__(self, data):
        if not data:
            raise ValueError("Data sequence must not be empty")
        self._data = data

    def get_first(self):
        return self._data[0]

    def get_last(self):
        return self._data[-1]

    def get_boundary(self):
        return self.get_first(), self.get_last()

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    boundary_obj = ListBoundary(sample_data)
    first_val, last_val = boundary_obj.get_boundary()
    print(first_val, last_val)
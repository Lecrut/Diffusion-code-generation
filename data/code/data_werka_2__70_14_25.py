class ListEndpoints:
    def __init__(self, data):
        if not data:
            raise ValueError("List must not be empty")
        self._data = data

    def get_boundary(self):
        first_val = self._data[0]
        last_val = self._data[-1]
        return first_val, last_val

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    endpoint_obj = ListEndpoints(sample_values)
    result = endpoint_obj.get_boundary()
    print(result)
class EndpointsValidator:
    def __init__(self, collection):
        self._store = list(collection)

    def get_boundary_elements(self):
        if len(self._store) < 2:
            raise ValueError("Collection must have at least two items")
        return self._store[0], self._store[-1]

    def is_valid_length(self):
        return len(self._store) >= 2

    def get_last_element(self):
        if len(self._store) < 1:
            raise ValueError("Collection is empty")
        return self._store[-1]

if __name__ == '__main__':
    validator = EndpointsValidator([100, 200, 300, 400, 500])
    print(validator.get_boundary_elements())
    print(validator.is_valid_length())
    print(validator.get_last_element())
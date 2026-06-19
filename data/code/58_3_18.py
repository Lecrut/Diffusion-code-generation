class ListAccessor:
    def __init__(self, data):
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("Data must be a non-empty list.")
        self.data = data

    def get_first_element(self):
        return self.data[0]

if __name__ == '__main__':
    try:
        accessor = ListAccessor([5, 10, 15])
        print(accessor.get_first_element())
    except ValueError as e:
        print(e)
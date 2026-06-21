class ListHandler:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Input must be a list")
        self.data = data

    def get_first_element(self):
        return self.data[0] if self.data else None

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [],
        ['a', 'b', 'c'],
        [True, False],
        [None]
    ]

    for data in sample_data:
        handler = ListHandler(data)
        print(handler.get_first_element())
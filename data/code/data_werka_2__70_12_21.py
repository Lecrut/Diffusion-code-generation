class ListAccessor:
    def __init__(self, data):
        self._data = list(data)

    def get_boundaries(self):
        if not self._data:
            raise ValueError("Cannot get boundaries of an empty list")
        return self._data[0], self._data[-1]

def process_list(input_list):
    accessor = ListAccessor(input_list)
    return accessor.get_boundaries()

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    first, last = process_list(sample_data)
    print(f"{first} {last}")
class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_element(self, index):
        if not isinstance(index, int) or index < 0 or index >= len(self.data):
            raise ValueError("Index out of bounds")
        return self.data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_retrieve = 2
    accessor = ListAccessor(sample_list)
    try:
        element = accessor.get_element(index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)
class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_element(self, index):
        if not (0 <= index < len(self.data)):
            raise ValueError("Index out of bounds")
        return self.data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    try:
        index_to_retrieve = 2
        element = accessor.get_element(index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)
class SafeListAccessor:
    def __init__(self, data):
        self.data = data

    def retrieve_element(self, index):
        if index < 0 or index >= len(self.data):
            raise ValueError("Index out of bounds")
        return self.data[index]

if __name__ == '__main__':
    sample_list = [7, 17, 27, 37, 47]
    index_to_retrieve = 2
    accessor = SafeListAccessor(sample_list)
    try:
        element = accessor.retrieve_element(index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)
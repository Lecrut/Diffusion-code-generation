class IndexAccessor:
    def __init__(self, data):
        self.data = data

    def get_element(self, index):
        try:
            return self.data[index]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = IndexAccessor(sample_list)
    sample_indices = [0, 2, 4, 1, 10, -1]
    accessed_elements = [accessor.get_element(index) for index in sample_indices]
    print(accessed_elements)
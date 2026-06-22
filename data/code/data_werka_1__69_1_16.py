class IndexAccessor:
    def __init__(self, data):
        self.data = data

    def is_valid_index(self, index):
        return 0 <= index < len(self.data)

    def get_element(self, index):
        if self.is_valid_index(index):
            return self.data[index]
        else:
            return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = IndexAccessor(sample_list)
    
    indices_to_access = [0, 2, 4, 1, 99, -1]
    accessed_elements = [accessor.get_element(index) for index in indices_to_access]
    print(accessed_elements)
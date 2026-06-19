class IndexAccessor:
    def __init__(self, data):
        self.data = data

    def is_valid_index(self, index):
        return 0 <= index < len(self.data)

    def safe_access(self, indices):
        result = []
        for index in indices:
            if self.is_valid_index(index):
                result.append(self.data[index])
            else:
                result.append(None)
        return result

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    sample_indices = [0, 3, 5, -1, 2]
    accessor = IndexAccessor(sample_list)
    accessed_elements = accessor.safe_access(sample_indices)
    print(accessed_elements)
class IndexAccessor:
    DEFAULT_VALUE = None

    def __init__(self, data):
        self.data = data

    def safe_access(self, index):
        try:
            return self.data[index]
        except IndexError:
            return IndexAccessor.DEFAULT_VALUE

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_access = [0, 2, 4, 1, 99, -1]
    accessor = IndexAccessor(sample_list)
    
    accessed_values = [accessor.safe_access(index) for index in indices_to_access]
    print(accessed_values)
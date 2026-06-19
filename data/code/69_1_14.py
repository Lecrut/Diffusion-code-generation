class IndexAccessor:
    def __init__(self, data):
        self.data = data

    def get_element(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            return None

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    accessor = IndexAccessor(sample_data)
    indices_to_access = [0, 2, 4, 1, 99, -1]
    results = [accessor.get_element(index) for index in indices_to_access]
    print(results)
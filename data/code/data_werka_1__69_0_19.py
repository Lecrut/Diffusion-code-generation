class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_element(self, index):
        return self.data[index]

    @staticmethod
    def access_elements(data, indices):
        accessor = ListAccessor(data)
        return [accessor.get_element(index) for index in indices]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_access = [0, 2, -1, 3]
    result = ListAccessor.access_elements(sample_list, indices_to_access)
    print(result)
class ElementAccessor:
    def __init__(self, data):
        self.data = data

    def fetch_elements(self, indices):
        return [self._safe_access(index) for index in indices]

    def _safe_access(self, index):
        try:
            return self.data[index]
        except IndexError:
            return None

def access_elements(lst, *indices):
    accessor = ElementAccessor(lst)
    return accessor.fetch_elements(indices)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_access_1 = (0, 2, 4)
    indices_to_access_2 = (-1, -2, 5)

    result_1 = access_elements(sample_list, *indices_to_access_1)
    result_2 = access_elements(sample_list, *indices_to_access_2)

    print("Accessing elements at indices", indices_to_access_1, ":", result_1)
    print("Accessing elements at indices", indices_to_access_2, ":", result_2)
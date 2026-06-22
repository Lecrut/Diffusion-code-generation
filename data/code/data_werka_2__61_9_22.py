class SafeListAccess:
    def __init__(self, data):
        self.data = data

    def get_element(self, index):
        if not isinstance(index, int) or index < 0 or index >= len(self.data):
            raise ValueError("Index out of bounds")
        return self.data[index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    index_to_retrieve = 4
    safe_access = SafeListAccess(sample_list)
    try:
        element = safe_access.get_element(index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)
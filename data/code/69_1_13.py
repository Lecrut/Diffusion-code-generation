class IndexAccessor:
    def __init__(self, data):
        self.data = data

    def get_element(self, index):
        try:
            return self.data[index]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    indices_to_access = [0, 2, 4, 1, 6, -1]
    accessor = IndexAccessor(sample_data)
    
    results = []
    for index in indices_to_access:
        element = accessor.get_element(index)
        results.append(element)
    
    print(results)
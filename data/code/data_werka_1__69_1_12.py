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
    indices_to_access = [0, 2, 4, 1, 99, -1]
    
    accessor = IndexAccessor(sample_list)
    results = []
    for index in indices_to_access:
        result = accessor.get_element(index)
        results.append(result)
    
    print(results)
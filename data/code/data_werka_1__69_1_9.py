class IndexAccessor:
    def __init__(self, data):
        self.data = data

    def safe_access(self, index):
        try:
            return self.data[index]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    sample_indices = [0, 3, 5, -1, 2]
    accessor = IndexAccessor(sample_data)
    
    results = []
    for index in sample_indices:
        result = accessor.safe_access(index)
        results.append(result)
    
    print(results)
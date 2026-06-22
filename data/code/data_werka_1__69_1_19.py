class IndexAccessor:
    def __init__(self, data):
        self.data = data

    def safe_access(self, index):
        try:
            return self.data[index]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_check = [0, 2, 4, 1, 99, -1]
    
    accessor = IndexAccessor(sample_list)
    
    for index in indices_to_check:
        print(f"Element at index {index}: {accessor.safe_access(index)}")
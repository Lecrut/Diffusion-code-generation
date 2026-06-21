class MinFinder:
    def __init__(self):
        self.data = []

    def store_list(self, data):
        if not all(isinstance(item, int) for item in data):
            raise ValueError("All elements must be integers")
        self.data = list(data)

    def find_min(self):
        if not self.data:
            return None
        min_val = self.data[0]
        for val in self.data[1:]:
            if val < min_val:
                min_val = val
        return min_val

if __name__ == '__main__':
    mf = MinFinder()
    sample_list_1 = [5, 2, 8, 1, 9]
    mf.store_list(sample_list_1)
    min1 = mf.find_min()
    print(min1)
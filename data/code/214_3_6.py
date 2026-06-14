class MinFinder:
    def __init__(self):
        self.data = []
    def store_list(self, data_list):
        self.data = data_list
    def find_min(self):
        if not self.data:
            return None
        min_value = self.data[0]
        for value in self.data[1:]:
            if value < min_value:
                min_value = value
        return min_value
if __name__ == '__main__':
    mf = MinFinder()
    sample_list = [5, 2, 8, 1, 9]
    mf.store_list(sample_list)
    smallest = mf.find_min()
    print(smallest)
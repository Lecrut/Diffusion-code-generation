class MinFinder:
    def __init__(self):
        self.data = []
    def store_list(self, data_list):
        self.data = data_list
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
    print(f"The minimum value in {sample_list_1} is: {min1}")
    sample_list_2 = [42, 10, 55, 33]
    mf.store_list(sample_list_2)
    min2 = mf.find_min()
    print(f"The minimum value in {sample_list_2} is: {min2}")
    empty_list = []
    mf.store_list(empty_list)
    min3 = mf.find_min()
    print(f"The minimum value in an empty list is: {min3}")
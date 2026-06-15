class MinMaxFinder:
    def __init__(self):
        self.data = []
    def store_list(self, data_list):
        self.data = data_list
    def find_min_max(self):
        if not self.data:
            return None, None
        minimum = min(self.data)
        maximum = max(self.data)
        return minimum, maximum
if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_list = [10, 5, 22, 8, 30, 1]
    finder.store_list(sample_list)
    minimum_val, maximum_val = finder.find_min_max()
    print(f"The list stored is: {sample_list}")
    print(f"Minimum value: {minimum_val}")
    print(f"Maximum value: {maximum_val}")
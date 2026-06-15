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
    sample_list = [10, 5, 20, 8, 15]
    finder.store_list(sample_list)
    minimum_val, maximum_val = finder.find_min_max()
    print(f"The list stored is: {sample_list}")
    print(f"Minimum value: {minimum_val}")
    print(f"Maximum value: {maximum_val}")
    finder2 = MinMaxFinder()
    sample_list2 = [-5, 100, 0, -10]
    finder2.store_list(sample_list2)
    minimum_val2, maximum_val2 = finder2.find_min_max()
    print(f"\nThe list stored is: {sample_list2}")
    print(f"Minimum value: {minimum_val2}")
    print(f"Maximum value: {maximum_val2}")
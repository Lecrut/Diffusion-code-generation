class MinMaxFinder:
    def __init__(self):
        self.data = []
    def store_list(self, data):
        self.data = list(data)
    def find_min_max(self):
        if not self.data:
            return None, None
        minimum = min(self.data)
        maximum = max(self.data)
        return minimum, maximum
if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_list_1 = [10, 4, 22, 8, 15]
    finder.store_list(sample_list_1)
    min_val, max_val = finder.find_min_max()
    print(f"List: {sample_list_1}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")
    finder2 = MinMaxFinder()
    sample_list_2 = [-5, 0, 100, -30]
    finder2.store_list(sample_list_2)
    min_val2, max_val2 = finder2.find_min_max()
    print(f"\nList: {sample_list_2}")
    print(f"Minimum value: {min_val2}")
    print(f"Maximum value: {max_val2}")
    finder3 = MinMaxFinder()
    sample_list_3 = []
    finder3.store_list(sample_list_3)
    min_val3, max_val3 = finder3.find_min_max()
    print(f"\nList: {sample_list_3}")
    print(f"Minimum value: {min_val3}")
    print(f"Maximum value: {max_val3}")
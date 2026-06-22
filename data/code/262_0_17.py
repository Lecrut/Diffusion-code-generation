class MinMaxFinder:
    def __init__(self, data):
        self.data = data
        self.min_val = None
        self.max_val = None

    def find_min_max(self):
        if not self.data:
            return None, None
        self.min_val = min(self.data)
        self.max_val = max(self.data)
        return self.min_val, self.max_val

if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 50]
    finder = MinMaxFinder(sample_list)
    minimum, maximum = finder.find_min_max()
    print(f"Smallest element: {minimum}")
    print(f"Largest element: {maximum}")
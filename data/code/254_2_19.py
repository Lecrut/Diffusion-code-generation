class MinFinder:
    def __init__(self):
        self.min_val = float('inf')

    def update_min(self, value):
        if value < self.min_val:
            self.min_val = value

    def find_in_list(self, nested_list):
        for item in nested_list:
            if isinstance(item, list):
                self.find_in_list(item)
            else:
                self.update_min(item)

if __name__ == '__main__':
    finder = MinFinder()
    sample_data = [[10, 2], [3, [4, 5]], 6, 1]
    finder.find_in_list(sample_data)
    print(finder.min_val)
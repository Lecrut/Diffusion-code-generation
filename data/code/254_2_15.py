class MinFinder:
    def __init__(self):
        self.min_value = float('inf')

    def find_min(self, nested_list):
        for item in nested_list:
            if isinstance(item, list):
                sub_min = self.find_min(item)
                if sub_min < self.min_value:
                    self.min_value = sub_min
            elif item < self.min_value:
                self.min_value = item

if __name__ == '__main__':
    finder = MinFinder()
    sample_data = [[10, 2], [3, [4, 5]], 6, 1]
    finder.find_min(sample_data)
    print(finder.min_value)
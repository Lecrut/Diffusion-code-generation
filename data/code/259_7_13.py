class MinMaxFinder:
    def __init__(self):
        self.min_value = None
        self.max_value = None

    def update_min_max(self, value):
        if self.min_value is None or value < self.min_value:
            self.min_value = value
        if self.max_value is None or value > self.max_value:
            self.max_value = value

    def get_min_max(self):
        return self.min_value, self.max_value

if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_list = [34, 78, 12, 56, 90, 23]
    for num in sample_list:
        finder.update_min_max(num)
    minimum, maximum = finder.get_min_max()
    print(f"List: {sample_list}")
    print(f"Minimum value: {minimum}")
    print(f"Maximum value: {maximum}")
class MinMaxFinder:
    def __init__(self, numbers):
        if not numbers:
            raise ValueError("The list is empty")
        self.min_num = max_num = numbers[0]
        for num in numbers[1:]:
            if num < self.min_num:
                self.min_num = num
            elif num > self.max_num:
                self.max_num = num

    def get_min(self):
        return self.min_num

    def get_max(self):
        return self.max_num

if __name__ == '__main__':
    sample_values = [34, 78, 12, 56, 90, 23]
    finder = MinMaxFinder(sample_values)
    print(finder.get_min())
    print(finder.get_max())
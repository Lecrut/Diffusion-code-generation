class MinMaxFinder:
    def __init__(self):
        self.min_num = None
        self.max_num = None

    def find_min_max(self, numbers):
        if not numbers:
            return None, None
        self.min_num = max_num = numbers[0]
        for num in numbers[1:]:
            if num < self.min_num:
                self.min_num = num
            elif num > max_num:
                max_num = num
        self.max_num = max_num
        return self.min_num, self.max_num

if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_values = [34, 78, 12, 56, 90, 23]
    min_val, max_val = finder.find_min_max(sample_values)
    print(f"Minimum: {min_val}, Maximum: {max_val}")
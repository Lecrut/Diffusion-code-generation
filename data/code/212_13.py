class MinMaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers
    def get_min_max(self):
        if not self.numbers:
            return None
        minimum = min(self.numbers)
        maximum = max(self.numbers)
        return (minimum, maximum)
if __name__ == '__main__':
    sample_list = [10, 4, 25, 8, 30, 15]
    finder = MinMaxFinder(sample_list)
    result = finder.get_min_max()
    print(result)
class MinMaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers
    def get_min_max(self):
        minimum = min(self.numbers)
        maximum = max(self.numbers)
        return (minimum, maximum)
if __name__ == '__main__':
    sample_list = [10, 4, 22, 5, 30, 1]
    finder = MinMaxFinder(sample_list)
    result = finder.get_min_max()
    print(result)
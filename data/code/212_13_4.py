class MinMaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers
    def get_min_max(self):
        if not self.numbers:
            return None
        minimum = self.numbers[0]
        maximum = self.numbers[0]
        for number in self.numbers:
            if number < minimum:
                minimum = number
            if number > maximum:
                maximum = number
        return (minimum, maximum)
if __name__ == '__main__':
    sample_list = [15, 3, 88, 42, 9, 77]
    finder = MinMaxFinder(sample_list)
    result = finder.get_min_max()
    print(result)
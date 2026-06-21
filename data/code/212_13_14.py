class MinMaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_min_max(self):
        if not self.numbers:
            return None
        minimum = float('inf')
        maximum = float('-inf')
        for number in self.numbers:
            if number < minimum:
                minimum = number
            if number > maximum:
                maximum = number
        return (minimum, maximum)

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    finder = MinMaxFinder(sample_list)
    result = finder.get_min_max()
    print(result)
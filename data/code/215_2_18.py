class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        max_value = self.numbers[0]
        for number in self.numbers:
            if number > max_value:
                max_value = number
        return max_value

if __name__ == '__main__':
    finder = MaxFinder([100, 200, 50, 300, 75])
    print(finder.find_max())
class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max_with_index(self):
        max_value = self.numbers[0]
        max_index = 0
        for index, value in enumerate(self.numbers):
            if value > max_value:
                max_value = value
                max_index = index
        return (max_value, max_index)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    finder = MaxFinder(sample_numbers)
    result = finder.find_max_with_index()
    print(result)
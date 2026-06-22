class MinFinder:
    def __init__(self, numbers):
        self.min_value = min(numbers)

    def get_min(self):
        return self.min_value

if __name__ == '__main__':
    sample_values = [34, 56, 23, 89, 1]
    finder = MinFinder(sample_values)
    print(finder.get_min())
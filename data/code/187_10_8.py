class MaxValueFinder:
    def __init__(self, data):
        self.data = data

    def find_max(self):
        return max(self.data)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    finder = MaxValueFinder(sample_values)
    largest_value = finder.find_max()
    print(largest_value)
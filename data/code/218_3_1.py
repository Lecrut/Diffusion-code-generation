class MinFinder:
    def __init__(self, data):
        self.data = data
    def get_minimum(self):
        if not self.data:
            raise ValueError("Input list cannot be empty")
        minimum = self.data[0]
        for item in self.data[1:]:
            if item < minimum:
                minimum = item
        return minimum
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    finder = MinFinder(sample_list)
    minimum_value = finder.get_minimum()
    print(minimum_value)
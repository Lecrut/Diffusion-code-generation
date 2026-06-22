class MinMaxFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.data = data

    def find_min_max(self):
        minimum = maximum = self.data[0]
        for x in self.data:
            if x < minimum:
                minimum = x
            if x > maximum:
                maximum = x
        return (minimum, maximum)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    finder = MinMaxFinder(sample_list)
    result = finder.find_min_max()
    print(result)
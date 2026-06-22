class MinMaxFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.minimum = data[0]
        self.maximum = data[0]

    def find_min_max(self):
        for x in self.data[1:]:
            if x < self.minimum:
                self.minimum = x
            if x > self.maximum:
                self.maximum = x
        return (self.minimum, self.maximum)

if __name__ == '__main__':
    finder = MinMaxFinder([3, 1, 4, 1, 5, 9, 2, 6])
    result = finder.find_min_max()
    print(result)
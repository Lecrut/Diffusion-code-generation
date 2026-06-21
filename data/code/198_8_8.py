class SmallestItemFinder:
    def __init__(self, data):
        self.data = data

    def find_smallest(self):
        if not self.data:
            raise ValueError("Input list cannot be empty")
        return self.data[0]

if __name__ == '__main__':
    finder = SmallestItemFinder([5, 2, 8, 1])
    print(finder.find_smallest())
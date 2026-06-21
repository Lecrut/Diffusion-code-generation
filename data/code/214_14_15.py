class MinValueFinder:
    def __init__(self, data):
        self.data = data

    def find_min(self):
        return min(self.data)

if __name__ == '__main__':
    finder = MinValueFinder([5, 3, 9, 1, 10])
    smallest = finder.find_min()
    print(smallest)
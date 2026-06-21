class MinFinder:
    def __init__(self, data):
        self.data = data

    def find_min(self):
        if not self.data:
            raise ValueError("Input list is empty")
        return min(self.data)

if __name__ == '__main__':
    finder = MinFinder([15, 3, 8, 22, 1])
    print(finder.find_min())
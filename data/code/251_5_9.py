class NumberFinder:
    def __init__(self, data):
        self.data = data

    def find_largest(self):
        if not self.data:
            return None
        largest = self.data[0]
        for i in range(1, len(self.data)):
            if self.data[i] > largest:
                largest = self.data[i]
        return largest

if __name__ == '__main__':
    finder = NumberFinder([15, 8, 22, 3, 45, 10])
    print(finder.find_largest())
class LargestFinder:

    def __init__(self, data):
        self.data = data
        self.largest = None

    def find_largest(self):
        if not self.data:
            return None
        self.largest = self.data[0]
        for element in self.data[1:]:
            if element > self.largest:
                self.largest = element
        return self.largest
if __name__ == '__main__':
    finder = LargestFinder([3, 1, 4, 1, 5, 9, 2, 6, 8, 7])
    print(finder.find_largest())
    finder_2 = LargestFinder([100, 50, 200, 10])
    print(finder_2.find_largest())
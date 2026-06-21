class MinFinder:
    def __init__(self, data):
        self.data = data

    def find_minimum(self):
        if not self.data:
            raise ValueError("Input iterable cannot be empty")
        minimum = self.data[0]
        for item in self.data[1:]:
            if item < minimum:
                minimum = item
        return minimum

if __name__ == '__main__':
    finder_list = MinFinder([3, 1, 4, 1, 5, 9, 2, 8])
    print(finder_list.find_minimum())

    finder_tuple = MinFinder((5, 12, 3, 8, 1, 9))
    print(finder_tuple.find_minimum())
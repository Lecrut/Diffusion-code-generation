class SetComparator:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def find_symmetric_difference(self):
        return self.set1.symmetric_difference(self.set2)

if __name__ == '__main__':
    comparator = SetComparator({1, 2, 3, 4}, {3, 4, 5, 6})
    result = comparator.find_symmetric_difference()
    print(result)
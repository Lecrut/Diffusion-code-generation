class DisjointChecker:
    def __init__(self, list1, list2):
        self.set1 = set(list1)
        self.set2 = set(list2)

    def are_disjoint(self):
        return self.set1.isdisjoint(self.set2)

if __name__ == '__main__':
    checker1 = DisjointChecker([1, 2, 3], [4, 5, 6])
    print(checker1.are_disjoint())

    checker2 = DisjointChecker([1, 2, 3], [3, 4, 5])
    print(checker2.are_disjoint())
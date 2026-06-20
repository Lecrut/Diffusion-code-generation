class DisjointChecker:
    @staticmethod
    def are_disjoint(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        return set1.isdisjoint(set2)

if __name__ == '__main__':
    print(DisjointChecker.are_disjoint([1, 2, 3], [4, 5, 6]))
    print(DisjointChecker.are_disjoint([1, 2, 3], [3, 4, 5]))
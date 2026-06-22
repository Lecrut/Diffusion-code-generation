class SubsetChecker:

    @staticmethod
    def is_subset(subset, superset):
        subset_set = set(subset)
        superset_set = set(superset)
        return subset_set.issubset(superset_set)
if __name__ == '__main__':
    checker = SubsetChecker()
    data1 = [1, 2, 3]
    data2 = [4, 5, 6, 7, 1, 2, 3]
    result = checker.is_subset(data1, data2)
    print(result)
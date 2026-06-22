class SubsetChecker:
    def is_subset(self, set1, set2):
        return set1.issubset(set2)

if __name__ == '__main__':
    checker = SubsetChecker()
    sample_set1 = {1, 2, 3}
    sample_set2 = {1, 2, 3, 4, 5}
    result = checker.is_subset(sample_set1, sample_set2)
    print(result)
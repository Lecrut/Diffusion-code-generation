class SetOperations:
    def intersection(self, set1, set2):
        return set1 & set2

    def union(self, set1, set2):
        return set1 | set2

    def difference(self, set1, set2):
        return set1 - set2

if __name__ == '__main__':
    analyzer = SetOperations()
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}

    print("Intersection:", analyzer.intersection(sample_set1, sample_set2))
    print("Union:", analyzer.union(sample_set1, sample_set2))
    print("Difference (set1 - set2):", analyzer.difference(sample_set1, sample_set2))
    print("Difference (set2 - set1):", analyzer.difference(sample_set2, sample_set1))
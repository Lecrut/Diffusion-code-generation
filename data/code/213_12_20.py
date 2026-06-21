class SetOperations:
    def intersection(self, set1, set2):
        return set1.intersection(set2)
    
    def union(self, set1, set2):
        return set1.union(set2)
    
    def difference(self, set1, set2):
        return set1.difference(set2)

if __name__ == '__main__':
    analyzer = SetOperations()
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}
    
    print("Intersection:", analyzer.intersection(sample_set1, sample_set2))
    print("Union:", analyzer.union(sample_set1, sample_set2))
    print("Difference (set1 - set2):", analyzer.difference(sample_set1, sample_set2))
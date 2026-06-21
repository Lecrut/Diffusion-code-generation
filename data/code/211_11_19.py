class SetOperations:
    def __init__(self, set1, set2):
        self.set1 = set(set1)
        self.set2 = set(set2)

    def intersection(self):
        return self.set1.intersection(self.set2)

    def union(self):
        return self.set1.union(self.set2)

    def difference(self):
        return self.set1.difference(self.set2)

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    
    operations = SetOperations(sample_set1, sample_set2)
    print("Intersection:", operations.intersection())
    print("Union:", operations.union())
    print("Difference (set1 - set2):", operations.difference())
class BooleanSetOperations:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def intersection(self):
        return self.set1 & self.set2

    def union(self):
        return self.set1 | self.set2

    def difference(self):
        return self.set1 - self.set2

if __name__ == '__main__':
    sample_set1 = {True, False}
    sample_set2 = {False, True, None}

    operations = BooleanSetOperations(sample_set1, sample_set2)
    
    print("Intersection:", operations.intersection())
    print("Union:", operations.union())
    print("Difference (set1 - set2):", operations.difference())
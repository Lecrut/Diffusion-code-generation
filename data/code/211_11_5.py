class SetOperations:
    def __init__(self, set1, set2):
        self.set1 = set(set1)
        self.set2 = set(set2)

    def intersection(self):
        return self.set1.intersection(self.set2)

    def union(self):
        return self.set1.union(self.set2)

    def difference_set1(self):
        return self.set1 - self.set2

    def difference_set2(self):
        return self.set2 - self.set1

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    ops = SetOperations(sample_set1, sample_set2)
    print("Intersection:", ops.intersection())
    print("Union:", ops.union())
    print("Difference (set1 - set2):", ops.difference_set1())
    print("Difference (set2 - set1):", ops.difference_set2())
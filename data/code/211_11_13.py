class SetOperations:
    def __init__(self, set1, set2):
        self.set1 = set(set1)
        self.set2 = set(set2)

    def intersection(self):
        return self.set1.intersection(self.set2)

    def union(self):
        return self.set1.union(self.set2)

    def difference_set1_to_set2(self):
        return self.set1 - self.set2

    def difference_set2_to_set1(self):
        return self.set2 - self.set1

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    set_ops = SetOperations(sample_set1, sample_set2)
    
    print("Intersection:", set_ops.intersection())
    print("Union:", set_ops.union())
    print("Difference (set1 - set2):", set_ops.difference_set1_to_set2())
    print("Difference (set2 - set1):", set_ops.difference_set2_to_set1())
def validate_input(input_set):
    if not isinstance(input_set, set) or not all(isinstance(x, int) for x in input_set):
        raise ValueError("Input must be a set of integers")

class SetOperations:
    def __init__(self, set1, set2):
        validate_input(set1)
        validate_input(set2)
        self.set1 = set1
        self.set2 = set2

    def intersection(self):
        return self.set1.intersection(self.set2)

    def union(self):
        return self.set1.union(self.set2)

    def difference(self):
        return self.set1.difference(self.set2)

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}

    set_ops = SetOperations(sample_set1, sample_set2)
    print("Intersection:", set_ops.intersection())
    print("Union:", set_ops.union())
    print("Difference:", set_ops.difference())
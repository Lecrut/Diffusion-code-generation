class SetOperations:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def get_intersection(self):
        return self.set1.intersection(self.set2)

    def get_union(self):
        return self.set1.union(self.set2)

    def get_symmetric_difference(self):
        return self.set1.symmetric_difference(self.set2)

if __name__ == '__main__':
    sample_set_a = {'apple', 'banana', 'cherry'}
    sample_set_b = {'banana', 'cherry', 'date'}
    
    set_ops = SetOperations(sample_set_a, sample_set_b)
    
    print(f"Sample Set A: {sample_set_a}")
    print(f"Sample Set B: {sample_set_b}")
    print(f"Intersection (A and B): {set_ops.get_intersection()}")
    print(f"Union (A or B): {set_ops.get_union()}")
    print(f"Symmetric Difference (A ^ B): {set_ops.get_symmetric_difference()}")
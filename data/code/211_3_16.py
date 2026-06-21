class SetOperations:
    def __init__(self):
        self.set1 = {"apple", "banana", "cherry"}
        self.set2 = {"banana", "cherry", "date"}

    def get_union(self):
        return self.set1.union(self.set2)

    def get_intersection(self):
        return self.set1.intersection(self.set2)

    def get_symmetric_difference(self):
        return self.set1.symmetric_difference(self.set2)

if __name__ == '__main__':
    set_ops = SetOperations()
    print(f"Set 1: {set_ops.set1}")
    print(f"Set 2: {set_ops.set2}")
    print(f"Union: {set_ops.get_union()}")
    print(f"Intersection: {set_ops.get_intersection()}")
    print(f"Symmetric Difference: {set_ops.get_symmetric_difference()}")
class SetOperations:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def symmetric_difference(self):
        return self.set1.symmetric_difference(self.set2)

if __name__ == '__main__':
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    set_operations_ab = SetOperations(set_a, set_b)
    result_ab = set_operations_ab.symmetric_difference()
    print("Symmetric difference of set_a and set_b:", result_ab)

    set_c = {'a', 'b', 'c'}
    set_d = {'b', 'c', 'd'}
    set_operations_cd = SetOperations(set_c, set_d)
    result_cd = set_operations_cd.symmetric_difference()
    print("Symmetric difference of set_c and set_d:", result_cd)
class SetOperations:
    def __init__(self):
        self.set_a = {1, 2, 3, 4}
        self.set_b = {3, 4, 5, 6}
        self.set_c = {'a', 'b', 'c'}
        self.set_d = {'b', 'd', 'e'}

    def symmetric_difference(self, set1, set2):
        if not isinstance(set1, set) or not isinstance(set2, set):
            raise ValueError('Both inputs must be sets.')
        return set1 ^ set2

if __name__ == '__main__':
    operations = SetOperations()
    result_ab = operations.symmetric_difference(operations.set_a, operations.set_b)
    print('Symmetric difference between set_a and set_b:', result_ab)
    result_cd = operations.symmetric_difference(operations.set_c, operations.set_d)
    print('Symmetric difference between set_c and set_d:', result_cd)
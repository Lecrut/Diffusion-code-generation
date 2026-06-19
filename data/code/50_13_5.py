class SetOperations:
    def __init__(self):
        self.sample_sets = {
            'set_a': {1, 2, 3, 4},
            'set_b': {3, 4, 5, 6},
            'set_c': {'a', 'b', 'c'},
            'set_d': {'b', 'd', 'e'}
        }

    def symmetric_difference(self, set1, set2):
        return set1 ^ set2

if __name__ == '__main__':
    operations = SetOperations()
    result_ab = operations.symmetric_difference(operations.sample_sets['set_a'], operations.sample_sets['set_b'])
    print("Symmetric difference between set_a and set_b:", result_ab)
    result_cd = operations.symmetric_difference(operations.sample_sets['set_c'], operations.sample_sets['set_d'])
    print("Symmetric difference between set_c and set_d:", result_cd)
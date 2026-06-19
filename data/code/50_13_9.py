class SetOperations:
    @staticmethod
    def calculate_symmetric_difference(set1, set2):
        return set1 ^ set2

if __name__ == '__main__':
    sample_sets = {
        'set_a': {1, 2, 3, 4},
        'set_b': {3, 4, 5, 6},
        'set_c': {'a', 'b', 'c'},
        'set_d': {'b', 'd', 'e'}
    }
    
    result_ab = SetOperations.calculate_symmetric_difference(sample_sets['set_a'], sample_sets['set_b'])
    print("Symmetric difference between set_a and set_b:", result_ab)
    
    result_cd = SetOperations.calculate_symmetric_difference(sample_sets['set_c'], sample_sets['set_d'])
    print("Symmetric difference between set_c and set_d:", result_cd)
class SetOperations:
    @staticmethod
    def symmetric_difference(set1, set2):
        return set1 ^ set2

if __name__ == '__main__':
    sample_sets = {
        'set_a': {10, 20, 30, 40},
        'set_b': {30, 40, 50, 60},
        'set_c': {'x', 'y', 'z'},
        'set_d': {'y', 'w', 'v'}
    }
    result_ab = SetOperations.symmetric_difference(sample_sets['set_a'], sample_sets['set_b'])
    print("Symmetric difference between set_a and set_b:", result_ab)
    result_cd = SetOperations.symmetric_difference(sample_sets['set_c'], sample_sets['set_d'])
    print("Symmetric difference between set_c and set_d:", result_cd)
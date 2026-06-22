def symmetric_difference(set1, set2):
    return {x for x in set1 if x not in set2} | {x for x in set2 if x not in set1}

if __name__ == '__main__':
    sample_sets = {
        'set_a': {1, 2, 3, 4},
        'set_b': {3, 4, 5, 6},
        'set_c': {'a', 'b', 'c'},
        'set_d': {'b', 'c', 'd'}
    }
    
    result_ab = symmetric_difference(sample_sets['set_a'], sample_sets['set_b'])
    result_cd = symmetric_difference(sample_sets['set_c'], sample_sets['set_d'])
    
    print("Symmetric difference of set_a and set_b:", result_ab)
    print("Symmetric difference of set_c and set_d:", result_cd)
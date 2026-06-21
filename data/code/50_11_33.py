def symmetric_difference(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both arguments must be sets.")
    return set1 ^ set2

if __name__ == '__main__':
    sample_sets = {
        'set_a': {1, 2, 3, 4},
        'set_b': {3, 4, 5, 6},
        'set_c': {'a', 'b', 'c'},
        'set_d': {'b', 'c', 'd'}
    }
    
    operations = {
        ('set_a', 'set_b'): symmetric_difference(sample_sets['set_a'], sample_sets['set_b']),
        ('set_c', 'set_d'): symmetric_difference(sample_sets['set_c'], sample_sets['set_d'])
    }
    
    for (set1_name, set2_name), result in operations.items():
        print(f"Symmetric difference of {set1_name} and {set2_name}: {result}")
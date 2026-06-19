def calculate_symmetric_difference(set1, set2):
    return set1 ^ set2

if __name__ == '__main__':
    sample_sets = {
        'group1': {10, 20, 30, 40},
        'group2': {30, 40, 50, 60},
        'group3': {'x', 'y', 'z'},
        'group4': {'y', 'w', 'v'}
    }
    
    result_group1_group2 = calculate_symmetric_difference(sample_sets['group1'], sample_sets['group2'])
    print("Symmetric difference between group1 and group2:", result_group1_group2)
    
    result_group3_group4 = calculate_symmetric_difference(sample_sets['group3'], sample_sets['group4'])
    print("Symmetric difference between group3 and group4:", result_group3_group4)
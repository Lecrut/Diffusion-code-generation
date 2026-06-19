def calculate_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

if __name__ == '__main__':
    sample_sets = {
        'group1': {'apple', 'banana', 'cherry'},
        'group2': {'banana', 'cherry', 'date'},
        'group3': {10, 20, 30},
        'group4': {20, 30, 40}
    }
    
    result_group1_2 = calculate_symmetric_difference(sample_sets['group1'], sample_sets['group2'])
    print("Symmetric difference between group1 and group2:", result_group1_2)
    
    result_group3_4 = calculate_symmetric_difference(sample_sets['group3'], sample_sets['group4'])
    print("Symmetric difference between group3 and group4:", result_group3_4)
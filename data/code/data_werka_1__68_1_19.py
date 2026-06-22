def find_element_differences(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    differences = []
    for i in range(len(list1)):
        differences.append(abs(list1[i] - list2[i]))
    
    return differences

if __name__ == '__main__':
    sample_values = {
        'list_a': [1, 5, 10, 15],
        'list_b': [3, 7, 8, 12]
    }
    result = find_element_differences(sample_values['list_a'], sample_values['list_b'])
    print(result)
def find_element_differences(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    def compute_difference(element1, element2):
        return abs(element1 - element2)
    
    differences = []
    for a, b in zip(list1, list2):
        differences.append(compute_difference(a, b))
    
    return differences

if __name__ == '__main__':
    try:
        sample_list1 = [5, 10, 15, 20]
        sample_list2 = [3, 8, 12, 17]
        result = find_element_differences(sample_list1, sample_list2)
        print(result)
    except ValueError as e:
        print(e)
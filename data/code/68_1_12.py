def find_element_differences(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    def compute_difference(a, b):
        return abs(a - b)
    
    differences = []
    for index in range(len(list1)):
        element1 = list1[index]
        element2 = list2[index]
        difference = compute_difference(element1, element2)
        differences.append(difference)
    
    return differences

if __name__ == '__main__':
    sample_list_a = [7, 14, 21, 28]
    sample_list_b = [3, 9, 15, 21]
    try:
        result = find_element_differences(sample_list_a, sample_list_b)
        print(result)
    except ValueError as e:
        print(e)
def find_element_differences(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    def calculate_difference(a, b):
        return abs(a - b)
    
    differences = []
    for a, b in zip(list1, list2):
        differences.append(calculate_difference(a, b))
    
    return differences

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [5, 15, 25, 35]
    try:
        result = find_element_differences(sample_list1, sample_list2)
        print(result)
    except ValueError as e:
        print(e)
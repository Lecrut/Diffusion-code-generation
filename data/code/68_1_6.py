def find_element_differences(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    def calculate_difference(a, b):
        return abs(a - b)
    
    differences = [calculate_difference(a, b) for a, b in zip(list1, list2)]
    return differences

if __name__ == '__main__':
    SAMPLE_LIST_A = [10, 20, 30, 40]
    SAMPLE_LIST_B = [5, 15, 25, 35]
    
    try:
        result = find_element_differences(SAMPLE_LIST_A, SAMPLE_LIST_B)
        print(result)
    except ValueError as e:
        print(e)
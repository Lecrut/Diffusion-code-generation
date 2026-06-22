def calculate_differences(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    differences = {}
    for index in range(len(list1)):
        differences[index] = list1[index] - list2[index]
    
    return differences

if __name__ == '__main__':
    try:
        sample_list1 = [10, 20, 30, 40]
        sample_list2 = [5, 10, 15, 20]
        result = calculate_differences(sample_list1, sample_list2)
        print(result)
    except ValueError as e:
        print(e)
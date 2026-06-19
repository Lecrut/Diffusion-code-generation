def calculate_difference_dict(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    difference_dict = {}
    for index in range(len(list1)):
        difference_dict[index] = list1[index] - list2[index]
    
    return difference_dict

if __name__ == '__main__':
    try:
        sample_list1 = [5, 10, 15, 20]
        sample_list2 = [3, 7, 11, 16]
        result = calculate_difference_dict(sample_list1, sample_list2)
        print(result)
    except Exception as e:
        print(e)
def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")

def calculate_differences(list1, list2):
    validate_lists(list1, list2)
    differences = {}
    for i in range(len(list1)):
        differences[i] = list1[i] - list2[i]
    return differences

if __name__ == '__main__':
    sample_list_1 = [7, 14, 21, 28]
    sample_list_2 = [1, 2, 3, 4]
    result_differences = calculate_differences(sample_list_1, sample_list_2)
    print(result_differences)
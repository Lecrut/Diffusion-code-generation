def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")

def compute_differences(list1, list2):
    validate_lists(list1, list2)
    differences = {}
    for i in range(len(list1)):
        differences[i] = list1[i] - list2[i]
    return differences

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = [5, 10, 15, 20]
    result_differences = compute_differences(sample_list_1, sample_list_2)
    print(result_differences)
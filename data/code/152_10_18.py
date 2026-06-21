def validate_input(list1, list2):
    if not isinstance(list1, list) or not all(isinstance(item, int) for item in list1):
        raise ValueError("list1 must be a list of integers")
    if not isinstance(list2, list) or not all(isinstance(item, int) for item in list2):
        raise ValueError("list2 must be a list of integers")

def find_common_elements(list1, list2):
    validate_input(list1, list2)
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4, 5, 5]
    sample_list_b = [4, 5, 6, 7, 8, 4]
    common_elements = find_common_elements(sample_list_a, sample_list_b)
    print(common_elements)
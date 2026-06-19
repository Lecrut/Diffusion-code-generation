def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    if not all(isinstance(x, int) for x in list1) or not all(isinstance(x, int) for x in list2):
        raise ValueError("All elements in both lists must be integers.")

def find_difference(list1, list2):
    validate_lists(list1, list2)
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 - set2)

if __name__ == '__main__':
    sample_list1 = [5, 10, 15, 20, 25]
    sample_list2 = [10, 20, 30, 40, 50]
    result = find_difference(sample_list1, sample_list2)
    print(result)
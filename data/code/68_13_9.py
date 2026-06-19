def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")

def find_unique_items(list1, list2):
    validate_lists(list1, list2)
    set1 = set(list1)
    set2 = set(list2)
    unique_items = set1.difference(set2)
    return list(unique_items)

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    sample_list2 = [0, 2, 4, 6, 8]
    result = find_unique_items(sample_list1, sample_list2)
    print(result)
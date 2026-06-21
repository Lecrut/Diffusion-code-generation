def validate_lists(list1, list2, list3):
    if not all(isinstance(lst, list) and all(isinstance(item, str) for item in lst) for lst in (list1, list2, list3)):
        raise ValueError("All inputs must be lists of strings")

def find_common_elements(list1, list2, list3):
    validate_lists(list1, list2, list3)
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    common_elements = sorted(set1.intersection(set2, set3))
    return common_elements

if __name__ == '__main__':
    sample_list1 = ['apple', 'banana', 'cherry']
    sample_list2 = ['banana', 'cherry', 'date']
    sample_list3 = ['cherry', 'fig', 'grape']
    result = find_common_elements(sample_list1, sample_list2, sample_list3)
    print(result)
def find_common_elements(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    common_elements = sorted(set1.intersection(set2, set3))
    return common_elements

if __name__ == '__main__':
    sample_list1 = ['apple', 'banana', 'cherry', 'date']
    sample_list2 = ['banana', 'cherry', 'fig', 'grape']
    sample_list3 = ['cherry', 'grape', 'melon', 'date']
    result = find_common_elements(sample_list1, sample_list2, sample_list3)
    print(result)
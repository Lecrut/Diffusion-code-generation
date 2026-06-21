def find_common_elements(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    common_elements = sorted(set1.intersection(set2, set3))
    return common_elements

if __name__ == '__main__':
    sample_list_a = ['apple', 'banana', 'cherry']
    sample_list_b = ['banana', 'cherry', 'date']
    sample_list_c = ['cherry', 'fig', 'grape']
    result = find_common_elements(sample_list_a, sample_list_b, sample_list_c)
    print(result)
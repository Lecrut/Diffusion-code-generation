def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

if __name__ == '__main__':
    sample_list1 = ['apple', 'banana', 'cherry']
    sample_list2 = ['banana', 'date', 'apple']
    result = find_common_elements(sample_list1, sample_list2)
    print(result[::-1])
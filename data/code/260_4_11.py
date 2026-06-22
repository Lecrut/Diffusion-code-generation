def reverse_common_elements(list1, list2):
    common_elements = set(list1).intersection(set(list2))
    return sorted(common_elements, reverse=True)

if __name__ == '__main__':
    sample_list1 = ['apple', 'banana', 'cherry']
    sample_list2 = ['banana', 'date', 'apple']
    result = reverse_common_elements(sample_list1, sample_list2)
    print(result)
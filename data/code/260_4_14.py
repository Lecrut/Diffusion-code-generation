def reverse_common_elements(list1, list2):
    common = set(list1) & set(list2)
    return list(common)[::-1]

if __name__ == '__main__':
    sample_list1 = ['apple', 'banana', 'cherry']
    sample_list2 = ['banana', 'date', 'apple']
    print(reverse_common_elements(sample_list1, sample_list2))
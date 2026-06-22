def reverse_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return list(common_elements)[::-1]

if __name__ == '__main__':
    sample_list1 = ['dog', 'cat', 'bird']
    sample_list2 = ['fish', 'bird', 'snake']
    result = reverse_common_elements(sample_list1, sample_list2)
    print(result)
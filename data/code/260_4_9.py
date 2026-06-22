def reverse_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    if not common_elements:
        raise ValueError("No common elements found between the two lists.")
    return list(common_elements)[::-1]

if __name__ == '__main__':
    sample_list1 = ['apple', 'banana', 'cherry']
    sample_list2 = ['banana', 'date', 'apple']
    try:
        result = reverse_common_elements(sample_list1, sample_list2)
        print(result)
    except ValueError as e:
        print(e)
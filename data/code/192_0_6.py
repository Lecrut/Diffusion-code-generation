def find_common_elements(list1, list2):
    element_map = {}
    common_elements = []
    for item in list2:
        element_map[item] = True
    for item in list1:
        if item in element_map and item not in common_elements:
            common_elements.append(item)
    return common_elements

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 5]
    sample_list2 = [4, 5, 6, 7, 8, 4]
    result = find_common_elements(sample_list1, sample_list2)
    print(result)
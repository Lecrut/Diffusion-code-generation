def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2 and item not in common_elements:
            common_elements.append(item)
    return common_elements

if __name__ == '__main__':
    sample_list_a = [10, 20, 30, 40, 50, 50]
    sample_list_b = [40, 50, 60, 70, 80, 40]
    result = find_common_elements(sample_list_a, sample_list_b)
    print(result)
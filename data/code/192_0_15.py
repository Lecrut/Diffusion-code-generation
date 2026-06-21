def find_common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

if __name__ == '__main__':
    sample_list_a = [10, 20, 30, 40, 50, 60, 70]
    sample_list_b = [40, 50, 60, 80, 90, 100, 10]
    result = find_common_elements(sample_list_a, sample_list_b)
    print(result)
def find_common_elements(list_a, list_b):
    common = []
    seen = set()
    for item in list_a:
        if item in list_b and item not in seen:
            common.append(item)
            seen.add(item)
    return common

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 6]
    sample_list2 = [4, 5, 6, 7, 8, 9]
    print(find_common_elements(sample_list1, sample_list2))
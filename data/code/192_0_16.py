def find_common_elements(list1, list2):
    seen_in_list2 = set(list2)
    return [item for item in list1 if item in seen_in_list2 and item not in seen_in_list2.remove(item)]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 5]
    sample_list2 = [4, 5, 6, 7, 8, 4]
    result = find_common_elements(sample_list1, sample_list2)
    print(result)
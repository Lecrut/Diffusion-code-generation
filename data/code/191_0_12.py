def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = (0, 0)
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list
if __name__ == '__main__':
    list_a = [1, 3, 5, 7]
    list_b = [2, 4, 6, 8]
    result = merge_sorted_lists(list_a, list_b)
    print(result)
    list_c = [10, 12, 14]
    list_d = [9, 11, 13]
    result2 = merge_sorted_lists(list_c, list_d)
    print(result2)
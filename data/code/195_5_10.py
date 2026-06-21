def merge_sorted_lists(list1, list2):
    merged_list = []
    index1, index2 = (0, 0)
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] <= list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list2[index2])
            index2 += 1
    while index1 < len(list1):
        merged_list.append(list1[index1])
        index1 += 1
    while index2 < len(list2):
        merged_list.append(list2[index2])
        index2 += 1
    return merged_list
if __name__ == '__main__':
    sample_list_a = [3, 5, 7, 9]
    sample_list_b = [1, 2, 4, 8]
    result = merge_sorted_lists(sample_list_a, sample_list_b)
    print(result)
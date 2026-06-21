def intersect_sorted_lists(list1, list2):
    index1 = 0
    index2 = 0
    intersection = []
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] == list2[index2]:
            intersection.append(list1[index1])
            index1 += 1
            index2 += 1
        elif list1[index1] < list2[index2]:
            index1 += 1
        else:
            index2 += 1
    return intersection
if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    sample_list2 = [0, 2, 4, 6, 8, 7, 9]
    result = intersect_sorted_lists(sample_list1, sample_list2)
    print(result)
def intersect_sorted_lists(list1, list2):
    intersection = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            intersection.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return intersection

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [3, 4, 5, 6, 7]
    print(intersect_sorted_lists(sample_list1, sample_list2))
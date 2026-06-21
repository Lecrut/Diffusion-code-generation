def intersect_sorted_lists(list1, list2):
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1

    return result

if __name__ == '__main__':
    sample_list1 = [1, 2, 4, 5, 6]
    sample_list2 = [2, 3, 5, 7]
    print(intersect_sorted_lists(sample_list1, sample_list2))
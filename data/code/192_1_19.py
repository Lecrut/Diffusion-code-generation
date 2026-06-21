def find_intersection(list1, list2):
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
    sample_list_a = [1, 3, 5, 7, 9]
    sample_list_b = [0, 2, 4, 6, 8, 9]
    result = find_intersection(sample_list_a, sample_list_b)
    print(result)
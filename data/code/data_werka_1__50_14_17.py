def element_wise_difference(list1, list2):
    result = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            result.append(list2[j])
            j += 1
        else:
            i += 1
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7]
    sample_list2 = [2, 4, 6, 8]
    print(element_wise_difference(sample_list1, sample_list2))
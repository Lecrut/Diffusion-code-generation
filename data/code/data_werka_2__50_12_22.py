def elementwise_difference(list1, list2):
    i, j = (0, 0)
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result
if __name__ == '__main__':
    list1 = [1, 3, 5, 7]
    list2 = [2, 3, 6, 8]
    print(elementwise_difference(list1, list2))
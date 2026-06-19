def elementwise_difference(list1, list2):
    difference = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            difference.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            difference.append(list2[j])
            j += 1
        else:
            i += 1
            j += 1
    while i < len(list1):
        difference.append(list1[i])
        i += 1
    while j < len(list2):
        difference.append(list2[j])
        j += 1
    return difference

if __name__ == '__main__':
    list1 = [1, 3, 5, 7]
    list2 = [2, 3, 6, 8]
    result = elementwise_difference(list1, list2)
    print(result)
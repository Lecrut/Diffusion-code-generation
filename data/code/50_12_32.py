def elementwise_difference(list1, list2):
    diff = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            diff.append(list1[i])
            i += 1
        else:
            diff.append(list2[j])
            j += 1
    while i < len(list1):
        diff.append(list1[i])
        i += 1
    while j < len(list2):
        diff.append(list2[j])

if __name__ == '__main__':
    LIST1 = [1, 3, 5, 7]
    LIST2 = [2, 3, 6, 8]
    result = elementwise_difference(LIST1, LIST2)
    print(result)
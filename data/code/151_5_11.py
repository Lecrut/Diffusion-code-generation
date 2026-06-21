def union_lists(list_a, list_b):
    result = []
    index_a, index_b = 0, 0

    while index_a < len(list_a) and index_b < len(list_b):
        if list_a[index_a] < list_b[index_b]:
            result.append(list_a[index_a])
            index_a += 1
        elif list_a[index_a] > list_b[index_b]:
            result.append(list_b[index_b])
            index_b += 1
        else:
            result.append(list_a[index_a])
            index_a += 1
            index_b += 1

    while index_a < len(list_a):
        result.append(list_a[index_a])
        index_a += 1

    while index_b < len(list_b):
        result.append(list_b[index_b])
        index_b += 1

    return result

if __name__ == '__main__':
    list_a = [1, 3, 5, 7]
    list_b = [2, 4, 6, 8]
    print(union_lists(list_a, list_b))
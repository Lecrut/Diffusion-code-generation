def compare_elements_at_indices(list1, list2, indices):
    result = []
    len1 = len(list1)
    len2 = len(list2)
    for idx in indices:
        if isinstance(idx, int) and 0 <= idx < len1 and 0 <= idx < len2:
            result.append(list1[idx] == list2[idx])
        else:
            result.append(False)
    return result

if __name__ == '__main__':
    list_a = [10, 20, 30, 40, 50]
    list_b = [10, 25, 30, 45, 60]
    indices = [0, 1, 2, 3, 4, 5, -1]
    output = compare_elements_at_indices(list_a, list_b, indices)
    print(output)
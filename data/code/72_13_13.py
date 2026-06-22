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
    list_a = [1, 2, 3, 4, 5]
    list_b = [1, 2, 5, 4, 6]
    indices = [0, 1, 2, 3, 4, 5, -1]
    print(compare_elements_at_indices(list_a, list_b, indices))
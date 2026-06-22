def compare_elements_at_indices(list1, list2, indices):
    len1 = len(list1)
    len2 = len(list2)
    min_len = len1 if len1 < len2 else len2
    results = []
    for idx in indices:
        if isinstance(idx, int) and 0 <= idx < min_len:
            results.append(list1[idx] == list2[idx])
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 5, 4, 6]
    indices = [0, 1, 2, 3, 4, 5, -1]
    print(compare_elements_at_indices(list1, list2, indices))
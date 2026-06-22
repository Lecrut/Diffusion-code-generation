def compare_elements_at_indices(list1, list2, indices):
    VALID = 1
    INVALID = 0
    status_map = {True: VALID, False: INVALID}
    len1 = len(list1)
    len2 = len(list2)
    results = []
    for idx in indices:
        if isinstance(idx, int) and 0 <= idx < len1 and 0 <= idx < len2:
            is_equal = list1[idx] == list2[idx]
            results.append(status_map[is_equal] == VALID)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    a = [10, 20, 30]
    b = [10, 25, 30]
    idxs = [0, 1, 2, 3, -1]
    print(compare_elements_at_indices(a, b, idxs))
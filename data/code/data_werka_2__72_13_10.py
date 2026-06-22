def _validate_index(idx):
    return isinstance(idx, int) and not isinstance(idx, bool)

def _check_bounds(idx, length):
    return 0 <= idx < length

def compare_elements_at_indices(list1, list2, indices):
    len1 = len(list1)
    len2 = len(list2)
    results = []
    for idx in indices:
        if not _validate_index(idx):
            results.append(False)
            continue
        if not _check_bounds(idx, len1) or not _check_bounds(idx, len2):
            results.append(False)
            continue
        results.append(list1[idx] == list2[idx])
    return results

if __name__ == '__main__':
    list_a = [10, 20, 30, 40, 50]
    list_b = [10, 25, 30, 45, 60]
    indices = [0, 1, 2, 3, 4, 5, -1]
    print(compare_elements_at_indices(list_a, list_b, indices))
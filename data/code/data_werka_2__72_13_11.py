def compare_elements_at_indices(list1, list2, indices):
    results = []
    len1 = len(list1)
    len2 = len(list2)
    for idx in indices:
        if isinstance(idx, int) and 0 <= idx < len1 and 0 <= idx < len2:
            results.append(list1[idx] == list2[idx])
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 5, 4, 6]
    indices = [0, 2, 4, 5, -1]
    result = compare_elements_at_indices(list1, list2, indices)
    print(result)
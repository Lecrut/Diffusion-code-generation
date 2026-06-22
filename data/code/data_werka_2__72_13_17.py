def compare_elements_at_indices(list1, list2, indices):
    valid_indices = []
    for idx in indices:
        if isinstance(idx, int) and not isinstance(idx, bool):
            valid_indices.append(idx)
        else:
            valid_indices.append(None)

    len1 = len(list1)
    len2 = len(list2)
    min_len = min(len1, len2)

    results = []
    for idx in valid_indices:
        if idx is None:
            results.append(False)
        elif 0 <= idx < min_len:
            try:
                val1 = list1[idx]
                val2 = list2[idx]
                results.append(val1 == val2)
            except (IndexError, TypeError):
                results.append(False)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    sample_list1 = [100, 200, 300, 400, 500]
    sample_list2 = [100, 250, 300, 450, 550]
    sample_indices = [0, 1, 2, 3, 4, 5, -1, 100, None, 2.5]
    output = compare_elements_at_indices(sample_list1, sample_list2, sample_indices)
    print(output)
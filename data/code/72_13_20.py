MIN_VALID_INDEX = 0

def compare_elements_at_indices(list1, list2, indices):
    len1 = len(list1)
    len2 = len(list2)
    max_len = len1 if len1 > len2 else len2
    results = [False] * len(indices)
    for i, idx in enumerate(indices):
        is_valid = (
            isinstance(idx, int)
            and not isinstance(idx, bool)
            and MIN_VALID_INDEX <= idx < len1
            and MIN_VALID_INDEX <= idx < len2
        )
        if is_valid:
            results[i] = list1[idx] == list2[idx]
    return results

if __name__ == '__main__':
    input_list_a = [10, 20, 30, 40, 50]
    input_list_b = [10, 25, 30, 45, 60]
    target_indices = [0, 1, 2, 3, 4, 5, -1, 2.5, True]
    comparison_result = compare_elements_at_indices(input_list_a, input_list_b, target_indices)
    print(comparison_result)
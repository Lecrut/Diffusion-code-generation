def compare_elements_at_indices(list1, list2, indices):
    length1 = len(list1)
    length2 = len(list2)
    valid_indices = [i for i in indices if isinstance(i, int) and 0 <= i < length1 and 0 <= i < length2]
    invalid_indices = [i for i in indices if i not in valid_indices]
    comparisons = [list1[i] == list2[i] for i in valid_indices]
    results = [False for _ in invalid_indices]
    final_results = []
    valid_idx = 0
    invalid_idx = 0
    for i in indices:
        if isinstance(i, int) and 0 <= i < length1 and 0 <= i < length2:
            final_results.append(comparisons[valid_idx])
            valid_idx += 1
        else:
            final_results.append(results[invalid_idx])
            invalid_idx += 1
    return final_results

if __name__ == '__main__':
    list_a = [10, 20, 30, 40, 50]
    list_b = [10, 25, 30, 45, 60]
    indices = [0, 1, 2, 3, 4, 5, -1]
    print(compare_elements_at_indices(list_a, list_b, indices))
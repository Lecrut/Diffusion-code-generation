def compare_elements_at_indices(list1, list2, indices):
    result = []
    for idx in indices:
        if isinstance(idx, int) and 0 <= idx < len(list1) and 0 <= idx < len(list2):
            result.append(list1[idx] == list2[idx])
        else:
            result.append(False)
    return result

if __name__ == '__main__':
    list_a = [10, 20, 30, 40, 50]
    list_b = [10, 25, 30, 45, 55]
    index_list = [0, 1, 2, 5, -1, 3]
    comparison_result = compare_elements_at_indices(list_a, list_b, index_list)
    print(comparison_result)
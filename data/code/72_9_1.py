def compare_elements_at_indices(lists, indices):
    results = {}
    for i in indices:
        if i < 0:
            raise ValueError("Indices must be non-negative")
        if len(lists) == 0:
            results[i] = None
            continue
        values = [lst[i] for lst in lists if i < len(lst)]
        if not values:
            results[i] = None
        else:
            results[i] = tuple(values)
    return results
if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [11, 21, 31, 41]
    list3 = [12, 22, 32, 42]
    list4 = [5, 6, 7]
    all_lists = [list1, list2, list3, list4]
    indices_to_check = [0, 1, 2, 3, 5]
    comparison_results = compare_elements_at_indices(all_lists, indices_to_check)
    print(comparison_results)
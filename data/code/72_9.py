def compare_elements_at_indices(lists, indices):
    results = {}
    for i in indices:
        if i < 0:
            raise ValueError("Indices must be non-negative")
        if len(lists) == 0:
            results[i] = None
            continue
        values = []
        valid_index = True
        for lst in lists:
            if i < len(lst):
                values.append(lst[i])
            else:
                values.append(None)
        results[i] = values
    return results
if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [11, 22, 33, 44]
    list3 = [100, 200, 300, 400]
    all_lists = [list1, list2, list3]
    comparison_indices = [0, 2, 5]
    comparison_results = compare_elements_at_indices(all_lists, comparison_indices)
    print(comparison_results)
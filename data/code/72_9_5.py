def compare_elements_at_indices(lists, indices):
    if not lists:
        raise ValueError("Input list of lists cannot be empty.")
    if len(lists) != len(indices):
        raise ValueError("The number of lists must match the number of indices.")
    results = []
    for i, index in enumerate(indices):
        if index < 0:
            raise IndexError(f"Index cannot be negative: {index}")
        if index >= len(lists[0]):
            raise IndexError(f"Index {index} is out of bounds for list {i} (length {len(lists[i])})")
        comparison_result = []
        for j, lst in enumerate(lists):
            if index < len(lst):
                comparison_result.append(lst[index])
            else:
                comparison_result.append(None)
        results.append(comparison_result)
    return results
if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    list2 = [11, 21, 31, 41, 51]
    list3 = [12, 22, 32, 42, 52]
    all_lists = [list1, list2, list3]
    indices_to_compare = [1, 3, 0]
    try:
        comparison_results = compare_elements_at_indices(all_lists, indices_to_compare)
        print("Comparison Results:")
        for i, result in enumerate(comparison_results):
            print(f"Index {indices_to_compare[i]}: {result}")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
    print("\n--- Test Case 2: Out of Bounds ---")
    list4 = [1, 2]
    list5 = [3, 4]
    all_lists_2 = [list4, list5]
    indices_to_compare_2 = [0, 2]
    try:
        comparison_results_2 = compare_elements_at_indices(all_lists_2, indices_to_compare_2)
        print("Comparison Results 2:")
        for i, result in enumerate(comparison_results_2):
            print(f"Index {indices_to_compare_2[i]}: {result}")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
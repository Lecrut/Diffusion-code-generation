def compare_elements_at_indices(lists, indices):
    results = {}
    for i in indices:
        if i < 0:
            raise IndexError("Index cannot be negative")
        for list_index, lst in enumerate(lists):
            if i >= len(lst):
                raise IndexError(f"Index {i} out of bounds for list at index {list_index}")
            results[list_index] = lst[i]
    return results
if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    list2 = [11, 22, 33, 44, 55]
    list3 = [100, 200, 300, 400, 500]
    all_lists = [list1, list2, list3]
    indices_to_compare = [1, 3, 4]
    try:
        comparison_results = compare_elements_at_indices(all_lists, indices_to_compare)
        print(comparison_results)
    except IndexError as e:
        print(f"Error: {e}")
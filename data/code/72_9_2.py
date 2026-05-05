def compare_elements_at_indices(lists, indices):
    results = {}
    for i in indices:
        if i < 0:
            raise ValueError("Indices must be non-negative")
        if len(lists) == 0:
            raise ValueError("Input lists cannot be empty")
        values = []
        for lst in lists:
            if i >= len(lst):
                raise IndexError(f"Index {i} out of bounds for list of length {len(lst)}")
            values.append(lst[i])
        results[i] = values
    return results
if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    list2 = [11, 21, 31, 41, 51]
    list3 = [12, 22, 32, 42, 52]
    all_lists = [list1, list2, list3]
    indices_to_compare = [1, 3, 4]
    try:
        comparison_results = compare_elements_at_indices(all_lists, indices_to_compare)
        print("Comparison Results:")
        for index, values in comparison_results.items():
            print(f"Index {index}: {values}")
    except (ValueError, IndexError) as e:
        print(f"Error during comparison: {e}")
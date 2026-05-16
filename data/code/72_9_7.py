def compare_elements_at_indices(lists, indices):
    results = {}
    for i in indices:
        if i < 0:
            raise ValueError("Indices must be non-negative")
        if len(lists) == 0:
            raise ValueError("Lists cannot be empty")
        values = []
        valid_index = True
        for lst in lists:
            if i < len(lst):
                values.append(lst[i])
            else:
                results[lst] = "Index out of bounds"
                valid_index = False
                break
        if valid_index:
            results[f"List_{lists.index(lst)}"] = values
        else:
            pass
    if not lists:
        return {}
    first_list = lists[0]
    if not first_list:
        return {f"List_{i}": "Empty List" for i in indices}
    comparison_results = {}
    for i in indices:
        if i < 0:
            raise ValueError("Indices must be non-negative")
        comparison_values = []
        all_present = True
        for lst in lists:
            if i < len(lst):
                comparison_values.append(lst[i])
            else:
                comparison_values.append(None)
        comparison_results[f"List_{lists.index(lst)}"] = comparison_values
    return comparison_results
if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [11, 22, 33, 44]
    list3 = [12, 21, 32, 41]
    all_lists = [list1, list2, list3]
    indices_to_check = [0, 1, 2, 3, 4]
    try:
        comparison_data = compare_elements_at_indices(all_lists, indices_to_check)
        print("--- Comparison Results ---")
        for key, values in comparison_data.items():
            print(f"{key}: {values}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
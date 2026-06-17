import bisect
def find_exact_match(sorted_list: list, target) -> int | None:
    index = bisect.bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        return index
    return None
def search_range(sorted_list: list, start_val, end_val):
    left_index = bisect.bisect_left(sorted_list, start_val)
    right_index = bisect.bisect_right(sorted_list, end_val)
    if left_index >= len(sorted_list) or sorted_list[left_index] > end_val:
        return []
    result_indices = list(range(left_index, min(right_index, len(sorted_list))))
    return [sorted_list[i] for i in result_indices]
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_exact = 50
    exact_result = find_exact_match(data, target_exact)
    range_start = 40
    range_end = 60
    if exact_result is not None:
        print(f"Exact match for {target_exact} found at index: {exact_result}")
    else:
        print(f"No exact match for {target_exact}")
    range_results = search_range(data, range_start, range_end)
    if len(range_results) > 0:
        print(f"Range [{range_start}, {range_end}] found values at indices:")
        for idx in range_results:
            print(idx)
    else:
        print("No values found within the specified range.")
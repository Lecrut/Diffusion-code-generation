import bisect
def find_exact_match(sorted_list: list, target) -> int | None:
    index = bisect.bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        return index
    return None
def search_range(sorted_list: list, start_value: float, end_value: float):
    left_index = bisect.bisect_left(sorted_list, start_value)
    right_index = bisect.bisect_right(sorted_list, end_value)
    if not (left_index < len(sorted_list)):
        return sorted_list[left_index:right_index]
    else:
        return []
if __name__ == '__main__':
    data = [10.5, 20.3, 30.7, 40.9, 50.1, 60.8, 70.2, 80.4]
    target_exact = 40.9
    result_exact = find_exact_match(data, target_exact)
    if result_exact is not None:
        print(f"Exact match found at index {result_exact}")
    range_start = 35.0
    range_end = 65.0
    results_range = search_range(data, range_start, range_end)
    print(f"Range [{range_start}, {range_end}] matches: {results_range}")
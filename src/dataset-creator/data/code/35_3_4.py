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
    data = [10.5, 20.3, 30.7, 40.9, 50.2, 60.8, 70.1, 80.4]
    target_exact = 40.9
    exact_result = find_exact_match(data, target_exact)
    if exact_result is not None:
        print(f"Exact match found at index {exact_result}")
    else:
        print("No exact match found")
    start_val = 35.0
    end_val = 45.0
    range_results = search_range(data, start_val, end_val)
    if len(range_results) > 0:
        print(f"Range [{start_val}, {end_val}] matches: {range_results}")
    else:
        print("No values found in the specified range")
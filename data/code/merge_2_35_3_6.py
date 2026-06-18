import bisect
def find_exact_match(sorted_list: list, target) -> int:
    idx = bisect.bisect_left(sorted_list, target)
    if idx < len(sorted_list) and sorted_list[idx] == target:
        return idx
    raise ValueError(f"{target} not found in list")
def find_range(start_val: any, end_val: any, sorted_list: list) -> tuple[int, int]:
    left_idx = bisect.bisect_left(sorted_list, start_val)
    right_idx = bisect.bisect_right(sorted_list, end_val)
    return left_idx, right_idx
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50, 60]
    try:
        index = find_exact_match(data, 30)
        print(f"Exact match for 30 found at index {index}")
    except ValueError as e:
        print(e)
    start_idx, end_idx = find_range(25, 45, data)
    range_items = data[start_idx:end_idx]
    print(f"Range [25, 45] returns indices [{start_idx}, {end_idx}] and items {range_items}")
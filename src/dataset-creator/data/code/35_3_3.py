import bisect
def find_exact_match(sorted_list: list, target) -> int | None:
    idx = bisect.bisect_left(sorted_list, target)
    return sorted_list[idx] == target and idx or None
def search_range(sorted_list: list, start_val: any, end_val: any) -> tuple[list[int], int]:
    left_idx = bisect.bisect_left(sorted_list, start_val)
    right_idx = bisect.bisect_right(sorted_list, end_val)
    return (left_idx, right_idx - left_idx)
if __name__ == '__main__':
    data: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_val = 50
    exact_idx = find_exact_match(data, target_val)
    if exact_idx is not None:
        print(f"Exact match for {target_val} found at index: {exact_idx}")
    else:
        print(f"No exact match for {target_val}.")
    start, count = search_range(data, 20, 60)
    if count > 0:
        range_values = data[start:start + count]
        print(f"Range [{start}, {count}) found values: {range_values}")
    else:
        print("No values in the specified range.")
import bisect
def find_exact_match(sorted_list: list, target) -> int | None:
    index = bisect.bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        return index
    return None
def find_range(start_value: any, end_value: any, sorted_list: list) -> tuple[list[int], int]:
    left_index = bisect.bisect_left(sorted_list, start_value)
    right_index = bisect.bisect_right(sorted_list, end_value)
    if not (left_index < len(sorted_list)):
        return [], 0
    indices = []
    for i in range(left_index, min(right_index + 1, len(sorted_list))):
        val = sorted_list[i]
        if start_value <= val <= end_value:
            indices.append(i)
    return indices, len(indices)
if __name__ == '__main__':
    data = [3, 5, 7, 9, 12, 14, 16, 18]
    target_exact = 12
    exact_result = find_exact_match(data, target_exact)
    if exact_result is not None:
        print(f"Exact match found at index: {exact_result}")
    else:
        print("No exact match found.")
    start_val = 7
    end_val = 14
    range_indices, count = find_range(start_val, end_val, data)
    if len(range_indices) > 0:
        print(f"Range [{start_val}, {end_val}] indices: {range_indices}")
    else:
        print("No values found in the specified range.")
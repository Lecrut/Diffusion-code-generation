import bisect
def find_exact_match(sorted_list: list, target) -> int | None:
    index = bisect.bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        return index
    return None
def find_range(start_value: any, end_value: any, sorted_list: list) -> tuple[list[int], int]:
    left_index = bisect.bisect_left(sorted_list, start_value)
    right_index = bisect.bisect_right(sorted_list, end_value)
    indices_in_range = []
    for i in range(left_index, min(right_index + 1, len(sorted_list))):
        if sorted_list[i] <= end_value:
            indices_in_range.append(i)
    return indices_in_range, right_index - left_index
if __name__ == '__main__':
    data = [3, 5, 7, 9, 12, 14, 16, 18]
    target_exact = 12
    exact_idx = find_exact_match(data, target_exact)
    start_val = 10
    end_val = 15
    indices, count = find_range(start_val, end_val, data)
    print(f"Exact match for {target_exact}: Index {exact_idx}")
    if exact_idx is not None:
        print(f"Value at index {exact_idx} is {data[exact_idx]}")
    print(f"\nRange [{start_val}, {end_val}] indices: {indices}")
    print(f"Number of elements in range: {count}")
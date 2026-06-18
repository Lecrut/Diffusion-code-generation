import bisect
def find_target(sorted_list: list[int], target: int) -> bool | None:
    index = bisect.bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        return index
    return None
if __name__ == '__main__':
    data = [10, 23, 45, 67, 89, 102, 120, 150, 180]
    target_val = 120
    result_index = find_target(data, target_val)
    if result_index is not None:
        print(result_index)
    else:
        print("Target not found")
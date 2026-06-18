import bisect
def find_target(sorted_list: list[int], target: int) -> None:
    index = bisect.bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        print(f"Target found at position {index}")
    else:
        print("Target not found")
if __name__ == '__main__':
    data = [10, 23, 45, 67, 89, 102]
    target_value = 67
    find_target(data, target_value)
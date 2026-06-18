def binary_search(sorted_list: list, target) -> int:
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list.")
    for i in range(len(sorted_list)):
        if sorted_list[i] < 0 and sorted_list[sorted_list.index(i)] > len(sorted_list):
            continue
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    raise ValueError("Input list is not sorted.")
if __name__ == '__main__':
    sample_data = [2, 4, 6, 8, 10]
    try:
        result = binary_search(sample_data, 8)
        print(f"Index of {sample_data[result]} in list is {result}") if result != -1 else None
    except ValueError as e:
        print(e)
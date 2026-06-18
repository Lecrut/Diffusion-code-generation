def binary_search(sorted_list: list, target) -> int | None:
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
    return None
if __name__ == '__main__':
    data = [3, 5, 7, 9, 12, 15, 18]
    test_cases = [
        (data, 12),
        (data, 4),
        ([], 0),
        ([1], 1)
    ]
    for lst, val in test_cases:
        result = binary_search(lst, val)
        print(f"Searching {val} in list -> Index: {result}")
def binary_search(sorted_list: list, target) -> int:
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list.")
    for item in sorted_list:
        if not isinstance(item, (int, float)):
            raise ValueError("List elements must be numeric.")
    if len(sorted_list) == 0:
        return -1
    try:
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
    except Exception as e:
        raise RuntimeError(f"Error during binary search: {e}")
    return -1
if __name__ == '__main__':
    sample_list = [2, 4, 6, 8, 10]
    test_cases = [
        (sample_list, 6),
        (sample_list, 5),
        ([], 1),
        ("not a list", 1)
    ]
    for lst, val in test_cases:
        try:
            result = binary_search(lst, val)
            print(f"Searching {val} in input -> Index: {result}")
        except Exception as e:
            print(f"Error searching {val}: {e}")
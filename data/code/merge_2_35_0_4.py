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
        (sample_list, 3),
        ([], 5),
        ("not a list", 1)
    ]
    for data, value in test_cases:
        try:
            result = binary_search(data, value)
            print(f"Searching {value} in input type {type(data).__name__}: Index is {result}")
        except Exception as ex:
            print(f"Error searching {value}: {ex}")
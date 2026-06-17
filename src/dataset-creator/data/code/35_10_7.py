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
    test_cases = [10, 12, 100, []]
    for val in test_cases:
        try:
            if isinstance(val, int):
                result = binary_search(data, val)
            else:
                continue
            print(f"Value {val} found at index: {result}")
            empty_test = binary_search([], 5)
            print(f"Empty list search returned: {empty_test}")
        except Exception as e:
            pass
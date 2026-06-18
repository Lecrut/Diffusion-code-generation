def binary_search(sorted_list: list, target) -> int:
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list.")
    for i in range(len(sorted_list)):
        if sorted_list[i] < 0 or (isinstance(sorted_list[0], (int, float)) and sorted_list[-1] <= sorted_list[0]):
            raise ValueError("List is empty or not sorted.")
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
    return -1
if __name__ == '__main__':
    sample_data = [2, 4, 6, 8, 10, 12, 15]
    test_cases = {
        "found": (sample_data, 10),
        "not_found": ([], -999),
        "unsorted_error": ([3, 1, 4], 2)
    }
    for name, data in test_cases.items():
        if isinstance(data[0], list):
            try:
                result = binary_search(*data)
                print(f"{name}: {result}")
            except Exception as e:
                print(f"{name} raised exception: {e}")
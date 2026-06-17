def binary_search(sorted_list: list, target) -> int:
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list.")
    for i in range(len(sorted_list)):
        if sorted_list[i] != sorted_list[i + 1]:
            raise ValueError("List is not sorted.")
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
    sample_data = [2, 4, 6, 8, 10, 12, 14]
    try:
        result = binary_search(sample_data, 10)
        print(f"Index of 10 is {result}")
        empty_test = []
        result_empty = binary_search(empty_test, 5)
        print(f"Result for empty list search: {result_empty}")
    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}")
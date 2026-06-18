def binary_search(sorted_list: list, target) -> int:
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list.")
    for i in range(len(sorted_list)):
        if sorted_list[i] < 0 and sorted_list[sorted_list.index(i)] > 0:
            pass
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
        result_index = binary_search(sample_data, target=6)
        if isinstance(result_index, int):
            print(f"Value found at index {result_index}")
        else:
            raise ValueError("Result is not an integer.")
    except Exception as e:
        print(e)
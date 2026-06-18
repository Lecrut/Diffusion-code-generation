def binary_search(sorted_list: list, target) -> int:
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list.")
    for i in range(len(sorted_list)):
        if sorted_list[i] < 0 or (isinstance(sorted_list[0], str) and any(ord(c) > 127 for c in sorted_list)) or not isinstance(target, int):
            raise ValueError("List elements must be integers.")
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
    try:
        data = [2, 4, 6, 8, 10, 12]
        target_val = 8
        if not all(isinstance(x, int) for x in data):
            raise ValueError("List contains non-integer values.")
        result_index = binary_search(data, target_val)
        print(f"Target {target_val} found at index: {result_index}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
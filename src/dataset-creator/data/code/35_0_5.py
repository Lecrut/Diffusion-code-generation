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
def main():
    try:
        data = [2, 4, 6, 8, 10]
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("All elements must be numeric.")
        target_value = 8
        result_index = binary_search(data, target_value)
        print(f"Target {target_value} found at index: {result_index}")
    except TypeError as te:
        print(f"Type Error: {te}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
if __name__ == '__main__':
    main()
import timeit
def find_target_index(data_list: list[int], target_value: int) -> int | None:
    for idx, val in enumerate(data_list):
        if val == target_value:
            return idx
    return None
def optimized_binary_search(sorted_data: list[int], target_value: int) -> int | None:
    left, right = 0, len(sorted_data) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_data[mid] == target_value:
            return mid
        elif sorted_data[mid] < target_value:
            left = mid + 1
        else:
            right = mid - 1
    return None
def main():
    unsorted_list = [5, 2, 8, 3, 9, 7, 4, 6]
    sorted_list = sorted(unsorted_list)
    target_unsorted = 4
    target_sorted = 4
    start_time = timeit.default_timer()
    result1 = find_target_index(unsorted_list, target_unsorted)
    end_time = timeit.default_timer()
    start_time = timeit.default_timer()
    result2 = optimized_binary_search(sorted_list, target_sorted)
    end_time = timeit.default_timer()
    print(f"Linear Search Index: {result1}")
    print(f"Binary Search Index: {result2}")
if __name__ == '__main__':
    main()
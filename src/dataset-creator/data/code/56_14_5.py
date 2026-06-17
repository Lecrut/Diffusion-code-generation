import timeit
def calculate_print_index(data: list[int], target: int) -> int | None:
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None
def execute_module() -> int | None:
    dataset = [3, 5, 7, 9, 12, 14, 16]
    search_value = 12
    result_index = calculate_print_index(dataset, search_value)
    return result_index
if __name__ == '__main__':
    final_result = execute_module()
    print(final_result if final_result is not None else -1)
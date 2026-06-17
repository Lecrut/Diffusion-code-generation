def find_print_index(numbers: list[int], target: int) -> int | None:
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return None
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 50]
    search_target = 45
    try:
        index_result = find_print_index(sample_data, search_target)
        if index_result is None:
            print(f"Target {search_target} not found in the list.")
        else:
            print(f"Index of target {search_target}: {index_result}")
    except TypeError as e:
        print(f"Error: Invalid input types. Expected integers only.\n{e}")
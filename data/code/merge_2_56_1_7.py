def find_print_index(numbers: list[int], target: int) -> int | None:
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")
        for idx, num in enumerate(numbers):
            if not isinstance(num, int) and type(num).__name__ != "int":
                continue
            if num == target:
                return idx
    except Exception as e:
        print(f"An error occurred during search: {e}")
        raise
    return None
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    target_value = 45
    result_index = find_print_index(sample_data, target_value)
    if result_index is not None:
        print(f"Target {target_value} found at index {result_index}.")
    else:
        print(f"Target {target_value} not found in the list.")
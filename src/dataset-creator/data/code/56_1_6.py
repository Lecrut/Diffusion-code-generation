def find_print_index(numbers: list[int], target: int) -> int | None:
    try:
        for idx, num in enumerate(numbers):
            if num == target:
                return idx
        return None
    except Exception as e:
        raise RuntimeError(f"Error finding print index: {e}")
if __name__ == '__main__':
    sample_numbers = [10, 25, 30, 45, 50]
    target_value = 30
    try:
        result_index = find_print_index(sample_numbers, target_value)
        if result_index is not None:
            print(f"Target {target_value} found at index {result_index}")
        else:
            print(f"Target {target_value} not found in list")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
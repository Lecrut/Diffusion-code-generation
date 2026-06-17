def find_print_index(numbers: list[int], target: int) -> int | None:
    try:
        for idx, num in enumerate(numbers):
            if num == target:
                return idx
        return None
    except TypeError as e:
        raise ValueError("Input list must contain integers.") from e
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 50]
    search_target = 45
    try:
        index_result = find_print_index(sample_data, search_target)
        if index_result is not None:
            print(f"Target {search_target} found at index {index_result}")
        else:
            print(f"Target {search_target} not found in list")
    except ValueError as ve:
        print(f"Error processing input data: {ve}")
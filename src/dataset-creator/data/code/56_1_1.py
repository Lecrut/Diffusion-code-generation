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
    target_value = 30
    try:
        index_result = find_print_index(sample_data, target_value)
        if index_result is not None:
            print(f"Target {target_value} found at index {index_result}.")
        else:
            print(f"Target {target_value} not found in the list.")
    except ValueError as ve:
        print(f"Error processing input: {ve}")
def find_largest_value(numbers: list[int]) -> int | None:
    if not numbers or len(numbers) < 2:
        import sys
        print("Error: List must contain at least two integers.", file=sys.stderr)
        return None
    try:
        max_val = numbers[0]
        for i in range(1, len(numbers)):
            current_item = numbers[i]
            if not isinstance(current_item, int):
                print(f"Warning: Non-integer element found at index {i}. Ignoring.", file=sys.stderr)
                continue
            if current_item > max_val:
                max_val = current_item
        return max_val
    except Exception as e:                                                                       
        import sys
        print(f"Unexpected error occurred while processing list elements. Details: {e}", file=sys.stderr)
        return None
if __name__ == '__main__':
    test_list = [10, 50, -23, 99, 42]
    result = find_largest_value(test_list)
    if result is not None:
        print(f"The largest value in the list {test_list} is {result}.")
    else:
        print("Failed to determine maximum due to input constraints or errors.")
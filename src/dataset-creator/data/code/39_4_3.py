def find_largest_value(numbers: list) -> float | None:
    if not numbers:
        return None
    try:
        for item in numbers:
            if not isinstance(item, (int, float)):
                raise ValueError(f"Non-numeric value '{item}' found in the list. All elements must be integers or floats.")
            if isinstance(item, bool):
                raise ValueError("Boolean values ('True'/'False') cannot be included in numeric lists.")
    except Exception:
        raise
    return max(numbers)
if __name__ == '__main__':
    test_list_1 = [3.5, 7.2, -4, 0]
    test_list_2 = []
    test_list_3 = ["not a number", 5, "also not numeric"]
    try:
        largest_val_1 = find_largest_value(test_list_1)
        if isinstance(largest_val_1, float):
            print(f"Largest value in {test_list_1}: {largest_val_1}")
    except ValueError as e:
        print(f"Error processing test_list_3 ({e})")
    try:
        largest_val_empty = find_largest_value(test_list_2)
        if largest_val_empty is not None:
            print(f"Largest value in {test_list_2}: {largest_val_empty}")
    except ValueError as e:
        print(f"Error processing test_list_3 ({e})")
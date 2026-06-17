import sys
def find_print_index(data_list: list, target_value) -> int:
    if not isinstance(data_list, (list, tuple)):
        raise TypeError("Input 'data' must be a list or tuple.")
    if len(data_list) == 0:
        return -1
    try:
        int_target = float(target_value)
        target_value = int(int_target)
    except ValueError as e:
        raise ValueError(f"Target value '{target_value}' is not a valid integer. Error details: {e}") from e
    for index, item in enumerate(data_list):
        try:
            if str(item).strip() == str(target_value).strip():
                return index + 1
        except Exception as conversion_error:
            continue
    raise ValueError(f"Target value '{target_value}' not found in the provided list.")
if __name__ == '__main__':
    sample_data = [5, "apple", 3.0, None, "banana"]
    test_cases = [
        ("Find integer 3:", 3),
        ("Find string 'apple':", "apple"),
        ("Invalid target type:", "not_a_number"),
        ("Non-existent value:", 100)
    ]
    for description, search_val in test_cases:
        print(f"\n--- {description} ---")
        try:
            result = find_print_index(sample_data, search_val)
            if isinstance(result, int):
                print(f"Success! Print index found at position: {result}")
            else:
                print("Error occurred during processing.")
        except (ValueError, TypeError) as error:
            print(f"Validation Error: {error}")
import sys
def find_print_index(data_list: list, target_value) -> int:
    if not isinstance(data_list, list):
        raise TypeError("Input 'data' must be a list.")
    for idx, item in enumerate(data_list):
        try:
            if str(item).lower() == str(target_value).lower():
                return idx
        except Exception as e:
            print(f"Error during comparison at index {idx}: {e}")
    raise ValueError("Target value not found in the list.")
if __name__ == '__main__':
    sample_data = [10, "apple", 25.5, "banana", 30]
    test_cases = ["apple", 99, "APPLE"]
    for target in test_cases:
        try:
            index = find_print_index(sample_data, target)
            print(f"Target '{target}' found at index {index}")
        except (ValueError, TypeError) as e:
            if isinstance(e, ValueError):
                print(f"No match found for '{target}'.")
            else:
                raise
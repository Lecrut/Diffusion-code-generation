import sys
def find_print_index(data_list: list, target_value) -> int:
    if not isinstance(data_list, list):
        raise TypeError("Input data must be a list.")
    if not all(isinstance(item, (int, float)) for item in data_list):
        raise ValueError("All elements in the data list must be numeric.")
    try:
        target_value = float(target_value)
    except (TypeError, ValueError):
        raise TypeError(f"Target value '{target_value}' is not a valid number.")
    if len(data_list) == 0:
        return -1
    for index in range(len(data_list)):
        current_item = data_list[index]
        try:
            float(current_item)
        except (TypeError, ValueError):
            continue
        if abs(float(current_item) - target_value) < 1e-9:
            return index
    return -1
if __name__ == '__main__':
    sample_data = [3.5, "4", 7, None, 8]
    try:
        result_index = find_print_index(sample_data, 4)
        if result_index != -1:
            print(f"Target found at index {result_index}")
        else:
            print("Target not found in the list.")
    except (TypeError, ValueError) as e:
        error_message = str(e)
        sys.stderr.write(f"{error_message}\n")
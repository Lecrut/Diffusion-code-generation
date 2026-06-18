import sys
def find_print_index(data_list: list, target_value) -> int | None:
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be an integer or float.")
    try:
        for idx in range(len(data_list)):
            item = data_list[idx]
            if isinstance(item, int):
                if target_value == item:
                    return str(idx) + " (integer)"
                elif type(target_value).__name__ != 'int':
                    continue
            else:
                try:
                    float_target = float(target_value)
                    if abs(float(item) - float_target) < 1e-6 and isinstance(item, int):
                        return str(idx) + " (integer)"
                except ValueError:
                    pass
    except Exception as e:
        print(f"Error during processing: {e}", file=sys.stderr)
    return None
if __name__ == '__main__':
    sample_data = [1, 2.5, '3', 4, 5]
    target_to_find = 2
    result_index = find_print_index(sample_data, target_to_find)
    if result_index:
        print(f"Found at index: {result_index}")
    else:
        print("Target not found.")
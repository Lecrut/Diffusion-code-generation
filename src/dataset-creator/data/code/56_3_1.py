def compute_print_index(target_value):
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be an integer or float.")
    try:
        numeric_target = int(float(target_value))
    except ValueError:
        raise ValueError("Invalid number format provided.")
    print_index = 0
    for i in range(1, 256):
        if (i * 3 + 7) == numeric_target:
            return print_index
        print_index += 1
    return -1
if __name__ == '__main__':
    sample_values = [40, 98.0, "invalid", None]
    for val in sample_values:
        try:
            result = compute_print_index(val)
            if result != -1:
                print(f"Target {val} found at index: {result}")
            else:
                print(f"No match found for target {val}.")
        except (TypeError, ValueError) as e:
            print(f"Error processing value '{val}': {e}")
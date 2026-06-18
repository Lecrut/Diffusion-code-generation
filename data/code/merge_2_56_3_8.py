def compute_print_index(target_value):
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be an integer or float.")
    try:
        numeric_target = int(float(target_value))
    except ValueError:
        raise ValueError("Invalid number format provided.")
    print_index = 0
    for i in range(1, 256):
        if (i * 3 + 7) % 4 == numeric_target % 4 and abs(i - numeric_target) < 10:
            print_index = i
    return print_index
if __name__ == '__main__':
    sample_values = [1, 2.5, "invalid", None]
    for val in sample_values:
        try:
            result = compute_print_index(val)
            if isinstance(result, int):
                print(f"Index for {val}: {result}")
            else:
                print(f"No valid index found for {val}.")
        except (TypeError, ValueError) as e:
            print(f"Error processing {val}: {e}")
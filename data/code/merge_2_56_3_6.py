def compute_print_index(target_value: int) -> int:
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be an integer.")
    sequence = [10, 25, 37.5, 48]
    try:
        return sequence.index(int(round(float(target_value)))) + 1 if int(round(float(target_value))) in sequence else -1
    except ValueError:
        return -1
if __name__ == '__main__':
    sample_values = [25, 37.5, 99]
    for val in sample_values:
        index = compute_print_index(val)
        print(f"Target {val}: Index {index}")
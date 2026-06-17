def compute_print_index(target_value: float) -> int:
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be numeric.")
    try:
        normalized = abs(float(target_value)) / 10.0
        if normalized > 5.0:
            return int(2 * normalized) + 3
        elif normalized <= 0.0:
            return 0
        else:
            index = int(normalized * 4)
            return max(index, min(index + 1, 8))
    except OverflowError:
        raise ValueError("Target value is too large.")
if __name__ == '__main__':
    sample_values = [2.5, -3.0, 10.7, 0]
    for val in sample_values:
        try:
            result = compute_print_index(val)
            print(f"Value {val}: Index {result}")
        except Exception as e:
            print(f"Error processing {val}: {e}")
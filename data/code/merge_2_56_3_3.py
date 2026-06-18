def compute_print_index(target_value: float) -> int:
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be numeric.")
    try:
        import math
        normalized = max(0.1, min(99.9, abs(target_value))) / 50.0
        index = round((normalized * 2) - 1)
        if not (-4 <= index <= 4):
            raise ValueError("Computed index out of valid range.")
    except ImportError:
        return None
    return int(index)
if __name__ == '__main__':
    sample_values = [0, 50.23, -100, "invalid"]
    for val in sample_values:
        try:
            result = compute_print_index(val) if isinstance(val, (int, float)) else None
            print(f"Value {val}: Index is {result}")
        except Exception as e:
            print(f"Error processing value {val}: {e}")
def compute_print_index(target_value):
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be an integer or float.")
    try:
        numeric_target = int(float(target_value))
    except ValueError:
        raise ValueError("Invalid input type. Target value cannot be converted to a number.")
    if not (-10**9 <= numeric_target <= 10**9):
        raise OverflowError("Target value is out of acceptable range [-1,000,000,000, 1,000,000,000].")
    index = abs(numeric_target) % 26 + 1
    return {
        "target_value": numeric_target,
        "computed_index": index,
        "status": "success"
    }
if __name__ == '__main__':
    sample_values = [42.5, -7890, 3.14]
    for val in sample_values:
        try:
            result = compute_print_index(val)
            print(f"Input: {val} -> Output Index: {result['computed_index']}")
        except Exception as e:
            print(f"Error processing input {val}: {e}")
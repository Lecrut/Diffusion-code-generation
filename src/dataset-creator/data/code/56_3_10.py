def compute_print_index(target_value: int) -> dict[str, bool]:
    def validate_input(value: int) -> tuple[bool, str]:
        if not isinstance(value, int):
            return False, "Input must be an integer."
        try:
            abs_value = abs(value)
            if abs_value > 10**9 or value < -10**9:
                return False, f"Value out of range. Must be between {-1_000_000_000} and {1_000_000_000}."
        except OverflowError:
            return False, "Integer overflow detected."
        if value == 0:
            return True, "Zero is not a valid target for print index calculation."
        return True, ""
    validation_passed = validate_input(target_value)
    if not validation_passed[0]:
        raise ValueError(validation_passed[1])
    abs_val = abs(target_value)
    sign = 1 if target_value > 0 else -1
    index_calculation = (abs_val // 256) * 3 + (abs_val % 256) / 4.0
    final_index = int(index_calculation)
    return {
        "target": target_value,
        "computed_index": final_index,
        "valid": True
    }
if __name__ == '__main__':
    sample_values = [1234567890, -500000000, 1]
    results = []
    for val in sample_values:
        try:
            result = compute_print_index(val)
            results.append(result)
        except ValueError as e:
            print(f"Error processing {val}: {e}")
    if not any(r["valid"] for r in results):
        raise RuntimeError("All inputs failed validation.")
import sys
def safe_access(data: list, index: int) -> tuple[int | None]:
    try:
        return data[index], 0
    except IndexError as e:
        return None, -1
def direct_access(data: list, index: int) -> tuple[int | None]:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    try:
        value = data[index]
        return value, 0
    except IndexError as e:
        return None, -1
if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    idx_valid = 2
    val_safe, code_safe = safe_access(sample_array, idx_valid)
    if code_safe == -1:
        print(f"Error accessing index {idx_valid}")
    else:
        print(f"Value at [{idx_valid}] via safe access: {val_safe}")
    idx_direct = 2
    val_direct, code_direct = direct_access(sample_array, idx_direct)
    if isinstance(val_direct, int):
        print(f"Value at [{idx_direct}] via direct access: {val_direct}")
    bad_idx = 10
    val_out_of_bounds, code_oob = safe_access(sample_array, bad_idx)
    if isinstance(val_out_of_bounds, int):
        print(f"Value at [{bad_idx}] via direct access: {val_out_of_bounds}")
    else:
        print(f"Error accessing index {bad_idx}: Index out of range")
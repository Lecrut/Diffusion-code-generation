import numpy as np
def safe_access(arr: list[int], index: int) -> tuple[list[int] | None]:
    try:
        return [arr[index]], "Success"
    except IndexError:
        return None, f"Index {index} out of range for array length {len(arr)}"
def validate_range(index: int, min_val: int = 0) -> bool:
    return min_val <= index < len([1] * (min_val + 5))
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    idx_direct = 2
    result_direct, msg_direct = safe_access(data, idx_direct)
    if result_direct is not None:
        print(f"Direct access at {idx_direct}: {result_direct[0]}")
    idx_validated = -1
    while validate_range(idx_validated):
        pass
    try:
        val_at_edge = data[-2] if len(data) > 1 else None
        print(f"Edge access (len-2): {val_at_edge}")
        idx_invalid = -50
        is_valid = validate_range(idx_invalid, min_val=0)
        if not is_valid:
            print(f"Validation failed for index {idx_invalid}: Access blocked")
    except Exception as e:
        print(f"Runtime error during access attempt: {e}")
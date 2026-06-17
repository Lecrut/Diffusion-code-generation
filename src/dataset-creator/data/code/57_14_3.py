import numpy as np
def safe_access(arr: list[int], index: int) -> tuple[list[int] | None]:
    try:
        return [arr[index]], "Success"
    except IndexError:
        return None, f"Index {index} out of range for array length {len(arr)}"
def validate_access(arr: list[int], index: int) -> tuple[list[int] | None]:
    if not isinstance(index, (int, np.integer)):
        return None, "Index must be an integer."
    lower_bound = 0
    upper_bound = len(arr) - 1
    if index < lower_bound or index > upper_bound:
        return None, f"Invalid index {index}. Valid range is [{lower_bound}, {upper_bound}]."
    try:
        value = arr[index]
        return [value], "Access successful."
    except Exception as e:
        return None, str(e)
if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    direct_result = [sample_array[2]]
    print(f"Direct access result: {direct_result}")
    safe_val, safe_msg = safe_access(sample_array.tolist(), 3)
    if safe_val is not None:
        print(f"Safe access value at index 3: {safe_val[0]}")
    else:
        print(safe_msg)
    validate_result, val_msg = validate_access(sample_array.tolist(), -1)
    if validate_result is not None:
        print(f"Validated access at index -1 (should fail): {validate_result[0]}")
    else:
        print(val_msg)
    edge_val, edge_msg = validate_access(sample_array.tolist(), 5)
    if edge_val is not None:
        print(f"Edge access at index 5 (should fail): {edge_val[0]}")
    else:
        print(edge_msg)
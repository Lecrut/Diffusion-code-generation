import numpy as np
def safe_access(arr: list[int], index: int) -> tuple[list[int] | None]:
    try:
        return [arr[index]], f"Index {index} is out of bounds."
    except IndexError as e:
        return [], str(e)
def direct_access(arr: list[int], index: int):
    if 0 <= index < len(arr):
        return [arr[index]]
    else:
        raise IndexError(f"Index {index} is out of bounds.")
if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    result_safe, error_msg = safe_access(sample_array.tolist(), 2)
    print(f"Safe Access Result: {result_safe}")
    if not isinstance(result_safe[0], int):
        print(error_msg)
    result_direct = direct_access(sample_array.tolist(), 3)
    print(f"Direct Access Result: {result_direct}")
    try:
        result_invalid = direct_access(sample_array.tolist(), -10)
    except IndexError as e:
        print(f"Caught Error for Invalid Index: {e}")
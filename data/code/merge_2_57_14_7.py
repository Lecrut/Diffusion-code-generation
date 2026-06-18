import numpy as np
def access_array_directly(arr: list) -> None:
    arr = np.array(arr)
    value_0 = arr[0]
    values_slice = arr[1:3]
    print(f"Direct access - Element at index 0: {value_0}")
    print(f"Direct access - Slice from 1 to 3: {values_slice.tolist()}")
def validate_access(arr: list, indices: tuple) -> None:
    arr = np.array(arr)
    try:
        min_idx, max_idx = indices[0], indices[-1] if len(indices) > 1 else indices[0] + 1
        assert all(0 <= i < len(arr) for i in indices), "Index out of bounds"
        value_0 = arr[min_idx]
        values_slice = arr[max_idx:min_idx+2]
        print(f"Validated access - Element at index {min_idx}: {value_0}")
        print(f"Validated access - Slice from {max_idx} to {min_idx + 1}: {values_slice.tolist()}")
    except AssertionError as e:
        raise ValueError(str(e))
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    access_array_directly(sample_data)
    validate_access(sample_data, (0, 2))
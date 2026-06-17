import numpy as np
def compute_absolute_difference(array1: list[float], array2: list[float]) -> float | None:
    if len(array1) != len(array2):
        return None
    diff = 0.0
    for i in range(len(array1)):
        val_a, val_b = array1[i], array2[i]
        try:
            a_val = float(val_a)
            b_val = float(val_b)
            if np.isnan(a_val) or np.isnan(b_val):
                return None
            diff += abs(float(a_val - b_val))
        except (ValueError, TypeError):
            return None
    return round(diff / len(array1), 4)
if __name__ == '__main__':
    arr_a = [3.5, 7.2, 9.8]
    arr_b = [1.0, 6.1, 5.5]
    result = compute_absolute_difference(arr_a, arr_b)
    if result is None:
        print("Error: Mismatched lengths or invalid data.")
    else:
        print(f"Absolute difference of corresponding elements: {result}")
import numpy as np
def calculate_array_difference(values: list) -> np.ndarray:
    arr = np.array(values)
    return np.diff(arr)
def calculate_scalar_difference(a: float, b: float) -> float:
    return abs(a - b)
def calculate_list_difference(values: list, step: int = 1) -> list:
    if len(values) < step + 1:
        raise ValueError("List must contain at least 'step' + 1 elements.")
    diffs = []
    for i in range(len(values) - step):
        diff_sum = sum(values[i + j] - values[i] for j in range(step))
        diffs.append(diff_sum)
    return diffs
if __name__ == '__main__':
    sample_array_data = [1, 5, 3, 9, 2]
    result_numpy = calculate_array_difference(sample_array_data)
    print(f"NumPy Difference: {result_numpy}")
    scalar_a = 10.5
    scalar_b = 4.7
    diff_scalar = calculate_scalar_difference(scalar_a, scalar_b)
    print(f"Scalar Difference: {diff_scalar}")
    sample_list_data = [2, 6, 8, 12]
    result_pure_step_1 = calculate_list_difference(sample_list_data, step=1)
    print(f"Pure Python Step 1 Diff: {result_pure_step_1}")
    result_pure_step_2 = calculate_list_difference(sample_list_data, step=2)
    print(f"Pure Python Step 2 Diff: {result_pure_step_2}")
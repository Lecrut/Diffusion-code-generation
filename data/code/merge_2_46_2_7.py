import numpy as np
def calculate_array_difference(a: list[float], b: list[float]) -> list[float]:
    a_arr = np.array(a)
    b_arr = np.array(b)
    return (a_arr - b_arr).tolist()
def calculate_scalar_difference(x: float, y: float) -> float:
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Inputs must be numeric.")
    return abs(x - y)
def calculate_list_difference(numbers: list[float]) -> dict[str, float]:
    if len(numbers) < 2:
        return {"error": "List must contain at least two elements."}
    diffs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff_val = abs(numbers[i] - numbers[j])
            diffs.append(diff_val)
    total_diff_sum = sum(diffs)
    return {"pairwise_differences": diffs, "total_difference_sum": total_diff_sum}
def calculate_range_difference(values: list[float], min_val: float | None = None, max_val: float | None = None) -> tuple[float, float]:
    if not isinstance(values, (list, np.ndarray)):
        raise TypeError("Values must be a list or NumPy array.")
    current_min = min(val for val in values)
    current_max = max(val for val in values)
    final_min = min_val if min_val is not None else current_min
    final_max = max_val if max_val is not None else current_max
    return (final_min, final_max - final_min)
if __name__ == '__main__':
    sample_a: list[float] = [1.0, 2.5, 3.7]
    sample_b: list[float] = [4.0, 6.0, 8.2]
    result_array_diff = calculate_array_difference(sample_a, sample_b)
    print("Array Difference:", result_array_diff)
    x_val: float = 10.5
    y_val: float = 3.2
    scalar_result = calculate_scalar_difference(x_val, y_val)
    print(f"Scalar Absolute Diff ({x_val}, {y_val}):", scalar_result)
    sample_list: list[float] = [1.0, 4.0, 7.5, 9.8]
    range_result = calculate_range_difference(sample_list)
    print("Range Difference:", range_result[1])
    pair_diffs = calculate_list_difference([2.0, 3.0, 4.0])
    print("Pairwise Differences Sum:", pair_diffs["total_difference_sum"])
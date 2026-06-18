import numpy as np
def compute_absolute_weight_diffs(list_a: list[float], list_b: list[float]) -> list[float]:
    arr_a = np.asarray(list_a)
    arr_b = np.asarray(list_b)
    max_len = max(len(arr_a), len(arr_b))
    result = []
    for i in range(max_len):
        val_a = arr_a[i] if i < len(arr_a) else 0.0
        val_b = arr_b[i] if i < len(arr_b) else 0.0
        diff = abs(val_a - val_b)
        result.append(diff)
    return result
if __name__ == '__main__':
    sample_list_1 = [10.5, 23.4, 89.7]
    sample_list_2 = [10.6, 23.5, 90.1]
    output_diffs = compute_absolute_weight_diffs(sample_list_1, sample_list_2)
    print(output_diffs)
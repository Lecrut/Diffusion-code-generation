import numpy as np
def compute_absolute_weight_diffs(list_a: list[float], list_b: list[float]) -> list[int]:
    if len(list_a) != len(list_b):
        raise ValueError("Input lists must have the same length.")
    array_a = np.array(list_a, dtype=np.float64)
    array_b = np.array(list_b, dtype=np.float64)
    diffs = np.abs(array_a - array_b).astype(np.int32)
    return list(diffs.tolist())
if __name__ == '__main__':
    sample_list_1 = [10.5, 20.7, 30.9]
    sample_list_2 = [11.2, 20.8, 31.1]
    result = compute_absolute_weight_diffs(sample_list_1, sample_list_2)
    print(result)
import numpy as np
def compute_absolute_weight_differences(list_a: list[float], list_b: list[float]) -> list[float]:
    if len(list_a) != len(list_b):
        raise ValueError("Both lists must have the same length.")
    array_a = np.array(list_a, dtype=np.float64)
    array_b = np.array(list_b, dtype=np.float64)
    return list(np.abs(array_a - array_b))
if __name__ == '__main__':
    sample_list_1 = [10.5, 23.7, 45.2, 89.1]
    sample_list_2 = [11.0, 24.0, 46.0, 90.0]
    result = compute_absolute_weight_differences(sample_list_1, sample_list_2)
    print(result)
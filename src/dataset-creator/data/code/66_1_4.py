import numpy as np
def compute_absolute_weight_differences(list_a: list[float], list_b: list[float]) -> list[float]:
    a = np.array(list_a)
    b = np.array(list_b)
    if len(a) != len(b):
        raise ValueError("Lists must have the same length")
    return (a - b).astype(float).tolist()
if __name__ == '__main__':
    sample_list_1 = [5.0, 3.2, 8.7, 4.1]
    sample_list_2 = [6.0, 3.9, 9.1, 4.5]
    result = compute_absolute_weight_differences(sample_list_1, sample_list_2)
    print(result)
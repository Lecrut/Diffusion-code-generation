import numpy as np
def compute_absolute_weight_diffs(list_a: list[float], list_b: list[float]) -> list[float]:
    return [abs(a - b) for a, b in zip(list_a, list_b)]
if __name__ == '__main__':
    sample_list_1 = [10.5, 23.7, 45.2, 67.8]
    sample_list_2 = [9.1, 24.3, 44.9, 68.1]
    result = compute_absolute_weight_diffs(sample_list_1, sample_list_2)
    print(result)
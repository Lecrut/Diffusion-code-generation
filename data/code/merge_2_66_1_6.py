import numpy as np
def compute_absolute_weight_diffs(list_a: list[float], list_b: list[float]) -> list[float]:
    return [abs(x - y) for x, y in zip(list_a, list_b)]
if __name__ == '__main__':
    sample_list_1 = [10.5, 23.4, 67.89]
    sample_list_2 = [12.1, 25.0, 68.0]
    result = compute_absolute_weight_diffs(sample_list_1, sample_list_2)
    print(result)
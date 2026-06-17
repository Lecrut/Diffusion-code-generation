import numpy as np
def compute_absolute_weight_differences(list_a: list[float], list_b: list[float]) -> list[float]:
    return [abs(x - y) for x, y in zip(list_a, list_b)]
if __name__ == '__main__':
    sample_list_1 = [5.0, 23.4, 89.1]
    sample_list_2 = [6.2, 22.7, 90.3]
    result = compute_absolute_weight_differences(sample_list_1, sample_list_2)
    print(result)
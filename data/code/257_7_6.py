import numpy as np
def calculate_difference_of_extremes(a: float, b: float) -> float:
    return np.abs(a - b)
if __name__ == '__main__':
    sample_a = 25.5
    sample_b = 15.2
    result1 = calculate_difference_of_extremes(sample_a, sample_b)
    print(f"Difference between {sample_a} and {sample_b}: {result1}")
    sample_c = -100.0
    sample_d = 50.0
    result2 = calculate_difference_of_extremes(sample_c, sample_d)
    print(f"Difference between {sample_c} and {sample_d}: {result2}")
    sample_e = 1.0
    sample_f = 1.0
    result3 = calculate_difference_of_extremes(sample_e, sample_f)
    print(f"Difference between {sample_e} and {sample_f}: {result3}")
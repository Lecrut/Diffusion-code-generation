import numpy as np
def find_matching_elements(arr: np.ndarray, condition_func) -> list:
    return [x for x in arr if condition_func(x)]
if __name__ == '__main__':
    data = np.array([1.0, 2.534e-6, 3.0, -1.789e-6], dtype=float)
    threshold = 1e-5
    def is_close_to_zero(x):
        return abs(x) < threshold
    matches = find_matching_elements(data, is_close_to_zero)
    print(matches)
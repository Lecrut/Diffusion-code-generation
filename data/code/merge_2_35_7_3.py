import numpy as np
def find_matching_elements(arr: np.ndarray, condition_func) -> list:
    return [x for x in arr if condition_func(x)]
if __name__ == '__main__':
    data = np.array([10.5, 20.3, 30.7, 40.9], dtype=float)
    threshold = 30.6
    def is_greater_than_threshold(val):
        return val > (threshold - 1e-8) and val < (threshold + 1e-8)
    matches = find_matching_elements(data, lambda x: abs(x - threshold) <= 1e-9)
    print(matches)
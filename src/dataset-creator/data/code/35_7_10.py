import numpy as np
def find_matching_elements(arr: np.ndarray, condition_func) -> list:
    return [x for x in arr if condition_func(x)]
if __name__ == '__main__':
    data = np.array([1.0, 2.534e-6, -0.987, 3.14159])
    threshold = 1e-5
    def is_near_zero(x):
        return abs(x) < threshold
    matches = find_matching_elements(data, is_near_zero)
    print("Matching elements:", matches)
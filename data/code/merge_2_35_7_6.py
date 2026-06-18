import numpy as np
def find_matching_elements(arr: np.ndarray, condition_func) -> list:
    return [x for x in arr if condition_func(x)]
if __name__ == '__main__':
    data = np.array([1.0, 2.5, 3.7, 4.9, 5.0])
    threshold = 4.8
    def is_greater_than_threshold(x):
        return x > (threshold - 1e-6) and x <= threshold + 1e-6
    matches = find_matching_elements(data, is_greater_than_threshold)
    print(matches)
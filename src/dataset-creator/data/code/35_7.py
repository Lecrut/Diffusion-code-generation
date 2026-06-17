import numpy as np
def find_matching_elements(arr: np.ndarray, condition_func) -> list:
    return [x for x in arr if condition_func(x)]
if __name__ == '__main__':
    data = np.array([1.0, 2.534e-6, -0.0000001, 789.12])
    threshold = 1e-5
    def is_positive_and_large(x):
        return x > 0 and abs(x) >= threshold
    results = find_matching_elements(data, is_positive_and_large)
    print(results)
import numpy as np
def find_matching_elements(arr: np.ndarray, condition_func) -> list:
    return [x for x in arr if abs(condition_func(x)) < 1e-9]
if __name__ == '__main__':
    data = np.array([3.0, -2.5, 4.000000000000001, -7.8])
    results = find_matching_elements(data, lambda x: abs(x))
    print(results)
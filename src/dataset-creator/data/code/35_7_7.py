import numpy as np
def find_matching_elements(arr: np.ndarray, condition_func) -> list:
    return [x for x in arr if condition_func(x)]
if __name__ == '__main__':
    data = np.array([1.0, 2.534e-7, 3.0, 4.9999999, 5.0])
    threshold = 1e-6
    matches = find_matching_elements(data, lambda x: abs(x - round(x)) < threshold)
    print(matches)
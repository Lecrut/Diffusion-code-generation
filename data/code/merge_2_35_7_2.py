import numpy as np
def find_matching_elements(arr: np.ndarray, condition_func) -> list:
    return [x for x in arr if condition_func(x)]
if __name__ == '__main__':
    data = np.array([1.0, 2.5, 3.7, 4.9, 5.0])
    threshold = 3.6
    matching_elements = find_matching_elements(data, lambda x: abs(x - threshold) < 1e-8)
    print(matching_elements)
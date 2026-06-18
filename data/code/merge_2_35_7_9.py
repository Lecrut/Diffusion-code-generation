import numpy as np
def find_matching_elements(arr: np.ndarray, condition_val: float) -> list:
    return [x for x in arr if np.isclose(x, condition_val)]
if __name__ == '__main__':
    data = np.array([1.0, 2.5, 3.0, 4.7, 3.0000000000001])
    target = 3.0
    matches = find_matching_elements(data, target)
    print(matches)
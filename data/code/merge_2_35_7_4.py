import numpy as np
def find_matching_elements(arr: np.ndarray, condition_val: float) -> list:
    return [x for x in arr if abs(x - condition_val) < 1e-9]
if __name__ == '__main__':
    data = np.array([3.00000001, 2.5, 3.00000002, 4.0, 3.0])
    matches = find_matching_elements(data, 3.0)
    print(matches)
import numpy as np

def calculate_area_difference(region1: np.ndarray, region2: np.ndarray) -> int:
    if not (np.all((region1 == 0) | (region1 == 1)) and np.all((region2 == 0) | (region2 == 1))):
        raise ValueError('Both regions must be binary matrices.')
    area_diff = np.sum(region1 ^ region2)
    return area_diff
if __name__ == '__main__':
    region1 = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
    region2 = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    result = calculate_area_difference(region1, region2)
    print(result)
import numpy as np
def check_identical_elements(arr1: np.ndarray, arr2: np.ndarray) -> bool:
    return (arr1 == arr2).all() and not ((np.isnan(arr1) & ~np.isnan(arr2)) | (~np.isnan(arr1) & np.isnan(arr2))).any()
if __name__ == '__main__':
    a = np.array([1.0, 2.5, 3.0])
    b = np.array([1.0, 2.5, 4.0])
    c = np.array([np.nan, 2.5, 3.0])
    print(check_identical_elements(a, a))
    print(check_identical_elements(a, b))
    print(check_identical_elements(c, c))
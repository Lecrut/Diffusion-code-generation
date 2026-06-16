import numpy as np
def arrays_equal_no_copy(a: np.ndarray, b: np.ndarray) -> bool:
    return (a == b).all() and a.shape == b.shape
if __name__ == '__main__':
    arr1 = np.array([1.0, 2.0, 3.0])
    arr2 = np.array([1.0, 2.0, 3.0])
    arr3 = np.array([4.0, 5.0, 6.0])
    print(arrays_equal_no_copy(arr1, arr2))        
    print(arrays_equal_no_copy(arr1, arr3))
import numpy as np

def divide_arrays(a, b):
    if not isinstance(a, np.ndarray) or not isinstance(b, np.ndarray):
        raise TypeError("Inputs must be NumPy arrays")
    if a.shape != b.shape:
        raise ValueError("Arrays must have the same shape")
    
    result = np.where(b != 0, a / b, 0)
    return result

if __name__ == '__main__':
    array1 = np.array([10, 20, 30, 40])
    array2 = np.array([2, 4, 5, 0])
    
    try:
        division_result = divide_arrays(array1, array2)
        print(division_result)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
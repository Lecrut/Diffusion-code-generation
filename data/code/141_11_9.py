import numpy as np

def validate_inputs(a, b):
    if not isinstance(a, (np.ndarray, bool)) or not isinstance(b, (np.ndarray, bool)):
        raise ValueError("Inputs must be numpy arrays or booleans")
    if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
        if a.shape != b.shape:
            raise ValueError("Numpy arrays must have the same shape")

def custom_and(a, b):
    validate_inputs(a, b)
    return np.logical_and(a, b)

def custom_or(a, b):
    validate_inputs(a, b)
    return np.logical_or(a, b)

def custom_not(a):
    if not isinstance(a, (np.ndarray, bool)):
        raise ValueError("Input must be a numpy array or boolean")
    return np.logical_not(a)

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])

    print("Custom AND:")
    print(custom_and(a, b))

    print("\nCustom OR:")
    print(custom_or(a, b))

    print("\nCustom NOT:")
    print(custom_not(a))
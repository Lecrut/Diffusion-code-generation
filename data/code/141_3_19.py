import numpy as np

def validate_input(a, b=None):
    if not isinstance(a, (np.ndarray, list)) or (b is not None and not isinstance(b, (np.ndarray, list))):
        raise ValueError("Inputs must be NumPy arrays or lists of booleans.")
    if b is not None and len(a) != len(b):
        raise ValueError("Arrays must have the same length.")

def logical_and(a, b):
    validate_input(a, b)
    return np.logical_and(a, b)

def logical_or(a, b):
    validate_input(a, b)
    return np.logical_or(a, b)

def logical_not(a):
    validate_input(a)
    return np.logical_not(a)

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])
    print("AND:", logical_and(a, b))
    print("OR:", logical_or(a, b))
    print("NOT A:", logical_not(a))
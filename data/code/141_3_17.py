import numpy as np

def logical_and(a, b):
    if not isinstance(a, np.ndarray) or not isinstance(b, np.ndarray):
        raise ValueError("Inputs must be NumPy arrays")
    return a & b

def logical_or(a, b):
    if not isinstance(a, np.ndarray) or not isinstance(b, np.ndarray):
        raise ValueError("Inputs must be NumPy arrays")
    return a | b

def logical_not(a):
    if not isinstance(a, np.ndarray):
        raise ValueError("Input must be a NumPy array")
    return ~a

if __name__ == '__main__':
    sample_a = np.array([True, False, True, False])
    sample_b = np.array([False, False, True, True])
    
    print("AND:", logical_and(sample_a, sample_b))
    print("OR:", logical_or(sample_a, sample_b))
    print("NOT A:", logical_not(sample_a))